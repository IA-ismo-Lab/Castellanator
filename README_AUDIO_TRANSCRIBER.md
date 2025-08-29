# 🎧 Audio Transcriber - AI-Powered Audio to Text Translator

[![By IA-ismo LAB](https://img.shields.io/badge/By-IA--ismo%20LAB-orange?style=for-the-badge)](https://github.com/IA-ismo-Lab)

**Professional AI tool** that converts audio files (MP3/M4A) to English text and translates them to Spanish. Perfect for understanding podcast content without generating audio output.

## ✨ Key Features

- 🎵 **Audio Processing** - Supports MP3, M4A, WAV, FLAC, AAC formats
- 📝 **Accurate Transcription** - OpenAI Whisper with smart language detection
- 🌍 **Professional Translation** - Google Gemini AI integration
- 📁 **Organized Output** - Timestamped folders prevent conflicts
- ⚡ **Fast Processing** - Optimized for various audio lengths
- 🛡️ **Professional Structure** - Clean, maintainable codebase

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Installation
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Test installation
test_audio.bat
```

### Usage
```bash
# Basic usage
python audio_transcriber.py "path/to/your/audio.mp3" "YOUR_GEMINI_API_KEY"

# Examples
python audio_transcriber.py podcast_episode.mp3 YOUR_API_KEY
python audio_transcriber.py "C:\Audio\interview.m4a" YOUR_API_KEY
```

## 📋 Supported Formats

- **MP3** - MPEG Audio Layer III
- **M4A** - MPEG-4 Audio
- **WAV** - Waveform Audio
- **FLAC** - Free Lossless Audio Codec
- **AAC** - Advanced Audio Coding

## 📂 Output Structure

After processing, your files are organized as follows:

```
transcriptions/
└── transcription_20231201_143022/
    ├── 📝 podcast_transcript.txt     # English transcription
    └── 🌍 podcast_spanish.txt        # Spanish translation
```

## 🔧 How It Works

1. **Load Audio** - Validates and loads the audio file
2. **Transcribe** - Converts speech to English text using Whisper
3. **Translate** - Translates to Spanish using Gemini AI
4. **Save Results** - Organizes output in timestamped folders

## ⚙️ Configuration

Create a `config.ini` file to customize settings:

```ini
[DEFAULT]
whisper_model = small        # tiny, base, small, medium, large
target_language = es         # Target language code
keep_temp_files = true       # Keep temporary files
verbose = true              # Show detailed output
output_folder = transcriptions  # Output folder name
```

## 🎯 Use Cases

- 🎧 **Podcast Analysis** - Understand foreign language podcasts
- 📚 **Content Review** - Review audio content in your language
- 🎓 **Language Learning** - Study pronunciation and vocabulary
- 💼 **Research** - Transcribe interviews and discussions
- 🌍 **Accessibility** - Make audio content accessible in text form

## 📊 Performance

- **Small Model**: Fast, good for clear audio
- **Medium Model**: Balanced speed/accuracy
- **Large Model**: Highest accuracy, slower processing

## 🛠️ Troubleshooting

### Common Issues

**"Model loading failed"**
- Check available RAM (Whisper models need 2-8GB)
- Try a smaller model in config.ini

**"API key invalid"**
- Verify your Gemini API key
- Check API quota and billing

**"Audio file not found"**
- Use absolute paths for audio files
- Ensure file is not corrupted

### Error Messages

- `❌ Audio file not found` - Check file path
- `❌ Unsupported format` - Use supported audio format
- `❌ API Error` - Check internet and API key

## 🤝 Contributing

Contributions welcome! This project is part of the IA-ismo LAB initiative.

## 📄 License

MIT License - see LICENSE file for details

---

**Made with ❤️ by IA-ismo LAB** | [GitHub](https://github.com/IA-ismo-Lab)
