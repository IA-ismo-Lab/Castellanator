import sys
import os
import yt_dlp
import whisper
from google import generativeai as genai
from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import make_chunks
from datetime import datetime

def create_process_folder():
    """Create a timestamped folder for this conversion process."""
    output_dir = "./output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    process_folder = os.path.join(output_dir, f"castellanator_{timestamp}")
    os.makedirs(process_folder)
    
    # Create temp folder for this process
    temp_dir = "./temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    return process_folder

def download_audio(url, output_path='audio'):
    """Download audio from YouTube URL using yt-dlp."""
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"Downloading: {percent} | Speed: {speed} | ETA: {eta}", end='\r')
        elif d['status'] == 'finished':
            print("\nDownload completed. Converting to MP3...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook],
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return output_path + '.mp3'
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None

def transcribe_audio(audio_path, model='small'):
    """Transcribe audio to text using Whisper."""
    print("Loading Whisper model (this may take a moment on first run)...")
    model = whisper.load_model(model, device='cpu')
    
    # Check audio duration
    audio = AudioSegment.from_mp3(audio_path)
    duration_minutes = len(audio) / 60000  # Convert to minutes
    print(f"Audio duration: {duration_minutes:.1f} minutes")
    
    if duration_minutes > 30:
        print("Audio is long (>30 min). Splitting into chunks for faster processing...")
        chunk_length_ms = 20 * 60 * 1000  # 20 minutes chunks
        chunks = make_chunks(audio, chunk_length_ms)
        
        full_transcript = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}...")
            chunk_path = f"./temp/temp_chunk_{i}.mp3"
            chunk.export(chunk_path, format="mp3")
            result = model.transcribe(chunk_path, verbose=False)
            full_transcript += result['text'] + " "
            # Keep temp files for debugging/analysis
        
        print("All chunks transcribed.")
        return full_transcript.strip()
    else:
        print("Transcribing audio... This may take several minutes depending on audio length.")
        result = model.transcribe(audio_path, verbose=True)
        return result['text']

def translate_text(text, api_key, target_lang='es'):
    """Translate text using Gemini API."""
    print("Connecting to Gemini API...")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Translate the following English text to Spanish: {text}"
    print("Translating text... Please wait.")
    response = model.generate_content(prompt)
    print("Translation completed.")
    return response.text

def text_to_speech(text, output_path='output.mp3', lang='es'):
    """Convert text to speech using gTTS."""
    print("Generating Spanish audio... This may take a moment.")
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_path)
    print("Audio generation completed.")
    return output_path

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <youtube_url> <gemini_api_key>")
        sys.exit(1)
    
    url = sys.argv[1]
    api_key = sys.argv[2]
    
    # Create process folder
    process_folder = create_process_folder()
    print(f"Created process folder: {process_folder}")
    
    # Step 1: Download audio
    print("\n=== STEP 1: Downloading audio ===")
    audio_path = download_audio(url, os.path.join(process_folder, 'audio'))
    print(f"Audio downloaded successfully: {audio_path}")
    
    # Step 2: Transcribe
    print("\n=== STEP 2: Transcribing audio ===")
    transcript = transcribe_audio(audio_path)
    transcript_path = os.path.join(process_folder, 'transcript.txt')
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write(transcript)
    print(f"Transcript saved to {transcript_path}")
    
    # Step 3: Translate
    print("\n=== STEP 3: Translating to Spanish ===")
    translated_text = translate_text(transcript, api_key)
    translated_path = os.path.join(process_folder, 'translated.txt')
    with open(translated_path, 'w', encoding='utf-8') as f:
        f.write(translated_text)
    print(f"Translated text saved to {translated_path}")
    
    # Step 4: Generate Spanish audio
    print("\n=== STEP 4: Generating Spanish audio ===")
    spanish_audio_path = text_to_speech(translated_text, os.path.join(process_folder, 'output.mp3'))
    print(f"Spanish audio saved to {spanish_audio_path}")
    
    print("\n🎉 All steps completed successfully!")
    print(f"All files saved in: {process_folder}")
    print("Files generated:")
    print(f"- {audio_path} (English audio)")
    print(f"- {transcript_path} (English transcript)")
    print(f"- {translated_path} (Spanish translation)")
    print(f"- {spanish_audio_path} (Spanish audio)")

if __name__ == "__main__":
    main()
