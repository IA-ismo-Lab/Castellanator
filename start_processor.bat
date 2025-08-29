@echo off
echo ============================================
echo Castellanator - AI Content Translator
echo ============================================
echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo.
echo Starting Castellanator...
echo.
python youtube_audio_processor.py
echo.
echo ============================================
echo SESSION COMPLETED
echo ============================================
echo.
echo Your files are saved in the 'output' folder:
echo 📁 %CD%\output\
echo.
echo Each conversion creates a timestamped folder with:
echo 🎵 audio.mp3 (Original audio)
echo 📝 transcript.txt (English transcript)
echo 🌍 translated.txt (Spanish translation)
echo 🔊 output.mp3 (Spanish audio)
echo.
echo PDF files should be placed in the 'pdf' folder.
echo.
pause
