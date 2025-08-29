#!/usr/bin/env python3
"""
🎧 Audio Transcriber - AI-Powered Audio to Text Translator

This script processes local audio files (MP3/M4A) and converts them to:
1. English transcription using OpenAI Whisper
2. Spanish translation using Google Gemini AI

Perfect for understanding podcast content without generating audio output.

Author: IA-ismo LAB
"""

import sys
import os
import whisper
from google import generativeai as genai
from datetime import datetime
import configparser

def load_config():
    """Load configuration from config.ini or use defaults."""
    config = configparser.ConfigParser()

    # Default settings
    config.add_section('DEFAULT')
    config.set('DEFAULT', 'whisper_model', 'small')
    config.set('DEFAULT', 'target_language', 'es')
    config.set('DEFAULT', 'keep_temp_files', 'true')
    config.set('DEFAULT', 'verbose', 'true')

    # Try to load from config file
    if os.path.exists('config.ini'):
        config.read('config.ini')
        print("✅ Configuration loaded from config.ini")
    else:
        print("⚠️  No config.ini found, using default settings")

    return config

def setup_ai_services(gemini_api_key):
    """Initialize AI services."""
    try:
        # Configure Gemini AI
        genai.configure(api_key=gemini_api_key)
        print("✅ Gemini AI configured")

        # Load Whisper model
        config = load_config()
        model_name = config.get('DEFAULT', 'whisper_model', fallback='small')
        print(f"🔄 Loading Whisper model: {model_name}")
        model = whisper.load_model(model_name)
        print("✅ Whisper model loaded")

        return model
    except Exception as e:
        print(f"❌ Error setting up AI services: {e}")
        return None

def transcribe_audio(model, audio_path):
    """Transcribe audio file to English text using Whisper."""
    try:
        print(f"🎵 Transcribing audio: {audio_path}")
        print("⏳ This may take a few minutes depending on audio length...")

        # Transcribe with Whisper
        result = model.transcribe(audio_path, language='en')

        transcription = result['text'].strip()
        print("✅ Transcription completed")
        print(f"📝 Transcription length: {len(transcription)} characters")

        return transcription
    except Exception as e:
        print(f"❌ Error transcribing audio: {e}")
        return None

def translate_text(text, target_language='es'):
    """Translate text to target language using Gemini AI."""
    try:
        print("🌍 Translating to Spanish...")
        print("⏳ Translation in progress...")

        # Create Gemini model
        model = genai.GenerativeModel('gemini-pro')

        # Create translation prompt
        prompt = f"""Translate the following English text to Spanish.
        Provide only the translation, without any additional comments or explanations.

        Text to translate:
        {text}

        Spanish translation:"""

        # Generate translation
        response = model.generate_content(prompt)
        translation = response.text.strip()

        print("✅ Translation completed")
        print(f"📝 Translation length: {len(translation)} characters")

        return translation
    except Exception as e:
        print(f"❌ Error translating text: {e}")
        return None

def save_results(audio_path, transcription, translation, output_folder):
    """Save transcription and translation to files."""
    try:
        # Get base filename without extension
        base_name = os.path.splitext(os.path.basename(audio_path))[0]

        # Save transcription
        transcript_file = os.path.join(output_folder, f"{base_name}_transcript.txt")
        with open(transcript_file, 'w', encoding='utf-8') as f:
            f.write(f"🎧 Audio Transcription - {base_name}\n")
            f.write(f"📅 Processed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"📁 Source: {audio_path}\n")
            f.write("="*60 + "\n\n")
            f.write("ENGLISH TRANSCRIPTION:\n")
            f.write("-"*30 + "\n")
            f.write(transcription)
        print(f"✅ Transcription saved: {transcript_file}")

        # Save translation
        translation_file = os.path.join(output_folder, f"{base_name}_spanish.txt")
        with open(translation_file, 'w', encoding='utf-8') as f:
            f.write(f"🎧 Audio Translation - {base_name}\n")
            f.write(f"📅 Processed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"📁 Source: {audio_path}\n")
            f.write("="*60 + "\n\n")
            f.write("SPANISH TRANSLATION:\n")
            f.write("-"*30 + "\n")
            f.write(translation)
        print(f"✅ Translation saved: {translation_file}")

        return transcript_file, translation_file
    except Exception as e:
        print(f"❌ Error saving results: {e}")
        return None, None

def create_output_folder():
    """Create timestamped output folder."""
    output_dir = "transcriptions"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Created folder: {output_dir}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    process_folder = os.path.join(output_dir, f"transcription_{timestamp}")
    os.makedirs(process_folder)
    print(f"📁 Created process folder: {process_folder}")

    return process_folder

def process_audio_file(audio_path, gemini_api_key):
    """Process a single audio file: transcribe and translate."""
    print("\n" + "="*60)
    print(f"🎧 Processing Audio File: {os.path.basename(audio_path)}")
    print("="*60)

    # Validate input file
    if not os.path.exists(audio_path):
        print(f"❌ Audio file not found: {audio_path}")
        return False

    # Check file extension
    valid_extensions = ['.mp3', '.m4a', '.wav', '.flac', '.aac']
    file_ext = os.path.splitext(audio_path)[1].lower()
    if file_ext not in valid_extensions:
        print(f"❌ Unsupported file format: {file_ext}")
        print(f"   Supported formats: {', '.join(valid_extensions)}")
        return False

    # Setup AI services
    model = setup_ai_services(gemini_api_key)
    if not model:
        return False

    # Create output folder
    output_folder = create_output_folder()

    # Transcribe audio
    transcription = transcribe_audio(model, audio_path)
    if not transcription:
        return False

    # Translate to Spanish
    translation = translate_text(transcription)
    if not translation:
        return False

    # Save results
    transcript_file, translation_file = save_results(
        audio_path, transcription, translation, output_folder
    )

    if transcript_file and translation_file:
        print("\n" + "="*60)
        print("✅ PROCESSING COMPLETED SUCCESSFULLY!")
        print("="*60)
        print(f"📁 Output folder: {output_folder}")
        print(f"📝 Transcription: {os.path.basename(transcript_file)}")
        print(f"🌍 Translation: {os.path.basename(translation_file)}")
        print("="*60)
        return True
    else:
        print("❌ Failed to save results")
        return False

def show_help():
    """Display help information."""
    print("\n" + "="*60)
    print("🎧 Audio Transcriber - Help")
    print("="*60)
    print("This tool transcribes audio files to English text and translates")
    print("them to Spanish using AI. Perfect for understanding podcasts!")
    print()
    print("USAGE:")
    print("  python audio_transcriber.py <audio_file> <gemini_api_key>")
    print("  python audio_transcriber.py --help")
    print()
    print("ARGUMENTS:")
    print("  audio_file    Path to audio file (MP3, M4A, WAV, FLAC, AAC)")
    print("  gemini_api_key  Your Google Gemini API key")
    print()
    print("EXAMPLES:")
    print("  python audio_transcriber.py podcast.mp3 YOUR_API_KEY")
    print("  python audio_transcriber.py \"C:\\audio\\episode.m4a\" YOUR_API_KEY")
    print()
    print("OUTPUT:")
    print("  Creates a timestamped folder in 'transcriptions/' with:")
    print("  - English transcription (.txt)")
    print("  - Spanish translation (.txt)")
    print("="*60)

def main():
    """Main function."""
    print("🎧 Audio Transcriber - AI-Powered Audio to Text Translator")
    print("   by IA-ismo LAB")
    print()

    # Parse command line arguments
    if len(sys.argv) < 2:
        show_help()
        return

    if sys.argv[1] in ['-h', '--help', 'help']:
        show_help()
        return

    if len(sys.argv) != 3:
        print("❌ Error: Incorrect number of arguments")
        print("   Use: python audio_transcriber.py <audio_file> <gemini_api_key>")
        print("   Or:  python audio_transcriber.py --help")
        return

    audio_path = sys.argv[1]
    gemini_api_key = sys.argv[2]

    # Process the audio file
    success = process_audio_file(audio_path, gemini_api_key)

    if success:
        print("\n🎉 Audio transcription and translation completed!")
        print("   You can now read the content in both English and Spanish.")
    else:
        print("\n❌ Processing failed. Check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
