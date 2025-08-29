@echo off
echo ============================================
echo Audio Transcriber - Example Usage
echo ============================================
echo.
echo This script demonstrates how to use the Audio Transcriber
echo with the sample audio file.
echo.
echo Press any key to continue...
pause >nul

echo.
echo Example 1: Process sample M4A file
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Example with sample file (you'll need to provide your own API key)
echo Processing sample audio file...
echo Command: python audio_transcriber.py "audio\Silicon_Valley_s_Techno-Faiths__From_Startup_Religions_to_Corporate_Cults_and_the_Shadow_of_AGI.m4a" YOUR_API_KEY
echo.
echo ⚠️  IMPORTANT: Replace YOUR_API_KEY with your actual Gemini API key
echo.
echo The script will:
echo 1. Load the Whisper AI model
echo 2. Transcribe the audio to English text
echo 3. Translate the text to Spanish
echo 4. Save both files in a timestamped folder
echo.

echo Example 2: Process your own audio file
echo.
echo python audio_transcriber.py "path\to\your\audio.mp3" YOUR_API_KEY
echo.

echo ============================================
echo Ready to transcribe audio files!
echo ============================================
echo.
pause
