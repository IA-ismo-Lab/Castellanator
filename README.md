# 🎧 Castellanator - AI-Powered YouTube Audio Translator

[![By Grok Code Fast](https://img.shields.io/badge/By-Grok%20Code%20Fast-blue?style=for-the-badge&logo=ai)](https://www.linkedin.com/newsletters/ia-ismo-7013065703138177024/)
[![IA-ismo LAB](https://img.shields.io/badge/IA--ismo-LAB-orange?style=for-the-badge)](https://www.linkedin.com/newsletters/ia-ismo-7013065703138177024/)

**Professional AI application** that transforms any YouTube video into Spanish audio content. Castellanator intelligently downloads English audio, transcribes it using advanced speech recognition, translates to Spanish with Gemini AI, and generates natural Spanish audio - perfect for professionals who want to consume content efficiently.

## ✨ Key Features

- 🤖 **AI-Powered Processing** - Advanced speech recognition and translation
- 🎵 **High-Quality Audio** - Best available format extraction
- 📝 **Accurate Transcription** - OpenAI Whisper with smart chunking
- 🌍 **Professional Translation** - Google Gemini AI integration
- 🔊 **Natural Voice Synthesis** - Google Text-to-Speech
- 📁 **Organized Workflow** - Timestamped outputs prevent conflicts
- ⚡ **Smart Optimization** - Automatic chunking for long videos
- 🛡️ **Professional Structure** - Clean, maintainable codebase

## ✨ Features

- 🚀 **One-click processing** - Just provide a YouTube URL
- 🎵 **High-quality audio download** - Best available audio format
- 📝 **Accurate transcription** - Powered by OpenAI Whisper
- 🌍 **Professional translation** - Using Google Gemini AI
- 🔊 **Natural Spanish audio** - Google Text-to-Speech
- 📁 **Organized outputs** - Timestamped folders prevent overwrites
- ⚡ **Smart chunking** - Handles long videos efficiently

## ⚙️ Installation

### Option 1: Automated Installation (Recommended)
```bash
# Double-click install.bat - It will:
# ✅ Create virtual environment
# ✅ Download yt-dlp.exe automatically
# ✅ Install all Python dependencies
install.bat
```

### Option 2: Manual Installation
```bash
# 1. Download yt-dlp.exe from: https://github.com/yt-dlp/yt-dlp/releases
# 2. Place it in the project folder
# 3. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

### Test Your Installation
```bash
# Verify everything is working:
test.bat
```

### Run Castellanator
```bash
# Double-click start_processor.bat or run:
python src/youtube_audio_processor.py "https://www.youtube.com/watch?v=VIDEO_ID" "YOUR_GEMINI_API_KEY"
```

### View Conversion History
```bash
# Run the hidden utility:
src/list_conversions.bat
```

### Cleanup Temporary Files
```bash
# Remove temporary processing files:
src/cleanup.bat
```

### Cleanup Temporary Files
```bash
# Remove temporary processing files:
src/cleanup.bat
```

## 📋 Requirements

- Python 3.8+
- FFmpeg (automatically handled by yt-dlp)
- Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 📂 Project Structure

```
Castellanator/
├── 📄 README.md              # Documentation
├── 📄 .gitignore             # Git ignore rules
├── 📄 requirements.txt       # Python dependencies
├── ⚙️ install.bat            # One-click installation
├── 🚀 start_processor.bat    # Main processor
└── 📁 src/                   # Source code
    ├── 🐍 youtube_audio_processor.py
    └── 📋 list_conversions.bat (hidden utility)
```

## 📂 Output Structure

After processing, your files are organized as follows:

```
output/
└── castellanator_20231201_143022/
    ├── 🎵 audio.mp3          # Original English audio
    ├── 📝 transcript.txt     # English transcription
    ├── 🌍 translated.txt     # Spanish translation
    └── 🔊 output.mp3         # Spanish audio

temp/
└── temp_chunk_*.mp3          # Processing chunks (kept for analysis)
```

## 🔧 How It Works

1. **Download** - Extracts audio from YouTube video
2. **Transcribe** - Converts speech to English text using Whisper
3. **Translate** - Translates to Spanish using Gemini AI
4. **Generate** - Creates Spanish audio using Google TTS

## 🎯 Professional Use Cases

- 💼 **Business Intelligence** - Stay updated with industry conferences in Spanish
- 🎓 **Continuous Learning** - Transform educational content for efficient consumption
- 🌍 **Language Professionals** - Create bilingual content for analysis
- ⏰ **Time Optimization** - Consume high-value content during commutes
- 📈 **Content Creation** - Generate Spanish versions of English content
- 🔬 **Research & Analysis** - Transcribe and translate for academic purposes

## 🤝 Contributing

Contributions welcome! This project is part of the AI-ismo LAB initiative.

## 📄 License

MIT License - feel free to use and modify!

---

**Made with ❤️ by IA-ismo LAB** | [Newsletter](https://www.linkedin.com/newsletters/ia-ismo-7013065703138177024/)
