@echo off
echo ============================================
echo Castellanator - YouTube Audio Translator
echo ============================================
echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo.
echo Enter your Gemini API key:
set /p api_key=
echo.
echo Enter the YouTube URL:
set /p url=
echo.
echo Processing... Please wait...
echo.
python src/youtube_audio_processor.py "%url%" "%api_key%"
echo.
echo ============================================
echo PROCESS COMPLETED SUCCESSFULLY!
echo ============================================
echo.
echo You can find your files in the 'output' folder:
echo 📁 %CD%\output\
echo.
echo Each conversion creates a timestamped folder with:
echo 🎵 audio.mp3 (Original English audio)
echo 📝 transcript.txt (English transcription)  
echo 🌍 translated.txt (Spanish translation)
echo 🔊 output.mp3 (Spanish audio)
echo.
echo Temporary files are kept in 'temp' folder for analysis.
echo.
pause
