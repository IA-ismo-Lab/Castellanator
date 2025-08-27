@echo off
echo ============================================
echo Castellanator - YouTube Audio Translator
echo ============================================
echo.
echo Installing Castellanator...
echo.

REM Check if virtual environment exists
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Download yt-dlp if not present
if not exist yt-dlp.exe (
    echo Downloading yt-dlp executable...
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe' -OutFile 'yt-dlp.exe'"
) else (
    echo yt-dlp.exe already exists.
)

REM Install Python requirements
echo Installing Python requirements...
pip install -r requirements.txt

echo.
echo ============================================
echo Installation completed successfully!
echo ============================================
echo.
echo To run Castellanator:
echo 1. Double-click start_processor.bat
echo 2. Or run: python src/youtube_audio_processor.py "YOUTUBE_URL" "GEMINI_API_KEY"
echo.
echo Project structure:
echo 📁 src/ - Source code
echo 📁 output/ - Your converted files
echo 📁 temp/ - Temporary processing files
echo.
pause
