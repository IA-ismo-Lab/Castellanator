import sys
import os
import yt_dlp
import whisper
from google import generativeai as genai
from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import make_chunks
from datetime import datetime
import PyPDF2
import pdfplumber

def show_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("🎧 Castellanator - AI Content Translator")
    print("="*50)
    print("Choose what you want to process:")
    print("1. 📺 YouTube Video")
    print("2. 📄 PDF Document")
    print("3. ❌ Exit")
    print("="*50)
    return input("Enter your choice (1-3): ").strip()

def create_folders():
    """Create necessary folders if they don't exist."""
    folders = ["output", "pdf"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"📁 Created folder: {folder}")

def create_process_folder():
    """Create a timestamped folder for this conversion process."""
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    process_folder = os.path.join(output_dir, f"castellanator_{timestamp}")
    os.makedirs(process_folder)
    
    # Create temp folder for this process
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    return process_folder

def select_pdf_file():
    """Let user select a PDF file from the pdf folder."""
    pdf_folder = "pdf"
    if not os.path.exists(pdf_folder):
        print(f"❌ PDF folder '{pdf_folder}' not found!")
        return None

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"❌ No PDF files found in '{pdf_folder}' folder!")
        print("Please place your PDF files in the 'pdf' folder and try again.")
        return None

    print(f"\n📄 Available PDF files in '{pdf_folder}':")
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"{i}. {pdf_file}")

    while True:
        try:
            choice = input(f"\nSelect PDF file (1-{len(pdf_files)}): ").strip()
            index = int(choice) - 1
            if 0 <= index < len(pdf_files):
                selected_file = os.path.join(pdf_folder, pdf_files[index])
                print(f"✅ Selected: {pdf_files[index]}")
                return selected_file
            else:
                print(f"❌ Please enter a number between 1 and {len(pdf_files)}")
        except ValueError:
            print("❌ Please enter a valid number")

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdfplumber (better for complex PDFs)."""
    print("📖 Extracting text from PDF...")
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"📄 Processing {total_pages} pages...")

            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                print(f"📄 Processed page {i+1}/{total_pages}", end='\r')

        print(f"\n✅ Extracted {len(text)} characters from PDF")
        return text.strip()

    except Exception as e:
        print(f"❌ Error extracting text from PDF: {e}")
        print("🔄 Trying alternative method with PyPDF2...")

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            print(f"✅ Extracted {len(text)} characters using alternative method")
            return text.strip()
        except Exception as e2:
            print(f"❌ Both extraction methods failed: {e2}")
            return None

def process_pdf(api_key):
    """Process a PDF file: extract text, translate, and convert to audio."""
    print("\n" + "="*50)
    print("📄 PDF Processing Mode")
    print("="*50)

    # Select PDF file
    pdf_path = select_pdf_file()
    if not pdf_path:
        return

    # Create process folder
    process_folder = create_process_folder()
    print(f"📁 Created process folder: {process_folder}")

    # Step 1: Extract text from PDF
    print("\n=== STEP 1: Extracting text from PDF ===")
    pdf_text = extract_text_from_pdf(pdf_path)
    if not pdf_text:
        print("❌ Failed to extract text from PDF")
        return

    # Save original text
    original_text_path = os.path.join(process_folder, 'original_text.txt')
    with open(original_text_path, 'w', encoding='utf-8') as f:
        f.write(pdf_text)
    print(f"📝 Original text saved to {original_text_path}")

    # Step 2: Translate text
    print("\n=== STEP 2: Translating to Spanish ===")
    translated_text = translate_text(pdf_text, api_key)

    # Save translated text
    translated_path = os.path.join(process_folder, 'translated.txt')
    with open(translated_path, 'w', encoding='utf-8') as f:
        f.write(translated_text)
    print(f"🌍 Translated text saved to {translated_path}")

    # Step 3: Generate Spanish audio
    print("\n=== STEP 3: Generating Spanish audio ===")
    spanish_audio_path = text_to_speech(translated_text, os.path.join(process_folder, 'output.mp3'))
    print(f"🔊 Spanish audio saved to {spanish_audio_path}")

    print("\n🎉 PDF processing completed successfully!")
    print(f"All files saved in: {process_folder}")
    print("Files generated:")
    print(f"- {original_text_path} (Original PDF text)")
    print(f"- {translated_path} (Spanish translation)")
    print(f"- {spanish_audio_path} (Spanish audio)")

def download_audio(url, output_path='audio'):
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
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path + '.mp3'

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
            chunk_path = f"temp/temp_chunk_{i}.mp3"
            chunk.export(chunk_path, format="mp3")
            result = model.transcribe(chunk_path, verbose=False)
            full_transcript += result['text'] + " "
            os.remove(chunk_path)  # Clean up
        
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

def process_youtube(api_key):
    """Process a YouTube video: download, transcribe, translate, and convert to audio."""
    print("\n" + "="*50)
    print("📺 YouTube Processing Mode")
    print("="*50)

    # Get YouTube URL
    url = input("Enter YouTube URL: ").strip()
    if not url:
        print("❌ No URL provided")
        return

    # Create process folder
    process_folder = create_process_folder()
    print(f"📁 Created process folder: {process_folder}")

    # Step 1: Download audio
    print("\n=== STEP 1: Downloading audio ===")
    audio_path = download_audio(url, os.path.join(process_folder, 'audio'))
    if not audio_path:
        print("❌ Failed to download audio")
        return
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

    print("\n🎉 YouTube processing completed successfully!")
    print(f"All files saved in: {process_folder}")
    print("Files generated:")
    print(f"- {audio_path} (English audio)")
    print(f"- {transcript_path} (English transcript)")
    print(f"- {translated_path} (Spanish translation)")
    print(f"- {spanish_audio_path} (Spanish audio)")

def main():
    """Main function with menu system."""
    print("\n" + "="*60)
    print("🎧 Castellanator - AI Content Translator")
    print("By IA-ismo LAB | Powered by Grok Code Fast")
    print("="*60)

    # Get Gemini API key
    api_key = input("Enter your Gemini API key: ").strip()
    if not api_key:
        print("❌ No API key provided")
        return

    # Create necessary folders
    create_folders()

    # Main menu loop
    while True:
        choice = show_menu()

        if choice == '1':
            process_youtube(api_key)
        elif choice == '2':
            process_pdf(api_key)
        elif choice == '3':
            print("\n👋 Thank you for using Castellanator!")
            print("Files are saved in the 'procesos' folder.")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

        print("\n" + "-"*50)
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
