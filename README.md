# 🎧 Castellanator - AI-Powered Content Translator

[![By Grok Code Fast](https://img.shields.io/badge/By-Grok%20Code%20Fast-blue?style=for-the-badge&logo=ai)](https://www.linkedin.com/newsletters/ia-ismo-7013065703138177024/)
[![IA-ismo LAB](https://img.shields.io/badge/IA--ismo-LAB-orange?style=for-the-badge)](https://www.linkedin.com/newsletters/ia-ismo-7013065703138177024/)

**Professional AI application** that transforms YouTube videos and PDF documents into Spanish audio content. Castellanator intelligently processes English content through advanced speech recognition and AI translation, generating natural Spanish audio - perfect for professionals who want to consume content efficiently in their preferred language.

## ✨ Key Features

- 🤖 **AI-Powered Processing** - Advanced speech recognition and translation
- 🎵 **Dual Content Support** - YouTube videos and PDF documents
- 📝 **Accurate Transcription** - OpenAI Whisper with smart chunking
- 🌍 **Professional Translation** - Google Gemini AI integration
- 🔊 **Natural Voice Synthesis** - Google Text-to-Speech
- 📄 **PDF Text Extraction** - Multiple extraction methods for reliability
- 📁 **Organized Workflow** - Timestamped outputs prevent conflicts
- ⚡ **Smart Optimization** - Automatic chunking for long content
- 🛡️ **Professional Structure** - Clean, maintainable codebase
- 🎯 **Interactive Menu** - User-friendly interface for easy operation

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

- 🚀 **One-click processing** - Just provide a YouTube URL or PDF file path
- 🎵 **High-quality audio download** - Best available audio format from YouTube
- 📄 **PDF text extraction** - Multiple methods for reliable text extraction
- 📝 **Accurate transcription** - Powered by OpenAI Whisper
- 🌍 **Professional translation** - Using Google Gemini AI
- 🔊 **Natural Spanish audio** - Google Text-to-Speech
- 📁 **Organized outputs** - Timestamped folders prevent overwrites
- ⚡ **Smart chunking** - Handles long videos and documents efficiently
- 🎯 **Interactive menu** - Easy-to-use interface for all operations

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
# Double-click start_processor.bat to open the interactive menu
# Or run directly:
python youtube_audio_processor.py
```

The interactive menu allows you to:
- Process YouTube videos
- Process PDF documents
- View conversion history
- Clean up temporary files

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

### Prepare for GitHub
```bash
# Prepare your project for GitHub publication:
prepare_github.bat
```

This script will:
- Initialize Git repository
- Add all project files
- Create professional commit message
- Provide instructions for GitHub upload

## 📋 Requirements

- Python 3.8+
- FFmpeg (automatically handled by yt-dlp)
- Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 📂 Project Structure

```
Castellanator/
├── 📄 README.md              # Documentation
├── 📄 LICENSE                # MIT License
├── 📄 requirements.txt       # Python dependencies
├── ⚙️ install.bat            # One-click installation
├── 🚀 start_processor.bat    # Main processor launcher
├── 🧪 test.bat               # System verification
├── 📁 output/                # Processed content outputs
├── 📁 pdf/                   # PDF processing workspace
├── 📁 temp/                  # Temporary processing files
└── 🐍 youtube_audio_processor.py  # Main application
```

## 📂 Output Structure

After processing, your files are organized as follows:

### YouTube Processing Output:
```
output/
└── castellanator_20231201_143022/
    ├── 🎵 audio.mp3          # Original English audio
    ├── 📝 transcript.txt     # English transcription
    ├── 🌍 translated.txt     # Spanish translation
    └── 🔊 output.mp3         # Spanish audio
```

### PDF Processing Output:
```
procesos/
└── conversion_20231201_143022/
    ├── 📄 original_text.txt  # Extracted text from PDF
    ├── 🌍 translated.txt     # Spanish translation
    └── 🔊 output.mp3         # Spanish audio
```

### Temporary Files:
```
temp/
└── temp_chunk_*.mp3          # Processing chunks (kept for analysis)

pdf/
└── [PDF workspace files]     # PDF processing workspace
```

## 🔧 How It Works

### YouTube Processing:
1. **Download** - Extracts audio from YouTube video
2. **Transcribe** - Converts speech to English text using Whisper
3. **Translate** - Translates to Spanish using Gemini AI
4. **Generate** - Creates Spanish audio using Google TTS

### PDF Processing:
1. **Extract** - Extracts text from PDF using multiple methods
2. **Translate** - Translates to Spanish using Gemini AI
3. **Generate** - Creates Spanish audio using Google TTS

### Interactive Menu:
- Choose between YouTube and PDF processing
- Enter URLs or file paths
- Configure API keys
- Monitor progress with real-time feedback

## 🎯 Professional Use Cases

- 💼 **Business Intelligence** - Stay updated with industry conferences and documents in Spanish
- 🎓 **Continuous Learning** - Transform educational content and research papers for efficient consumption
- 🌍 **Language Professionals** - Create bilingual content from videos and documents for analysis
- ⏰ **Time Optimization** - Consume high-value content during commutes and breaks
- 📈 **Content Creation** - Generate Spanish versions of English videos and documents
- 🔬 **Research & Analysis** - Transcribe, translate, and analyze academic content
- 📚 **Document Processing** - Convert technical papers and reports to audio format
- 🎧 **Accessibility** - Make written content accessible through audio conversion

## 🤝 Contributing

Contributions welcome! This project is part of the AI-ismo LAB initiative.

## 📄 License

MIT License - feel free to use and modify!

---

**Made with ❤️ by IA-ismo LAB** | [Newsletter](https://www.linkedin.com/newsletters/ia-ismo-7013065703138177024/)
