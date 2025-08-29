@echo off
echo ============================================
echo Castellanator - Quick Test
echo ============================================
echo.
echo This will test if all components are working.
echo It will test both YouTube and PDF processing capabilities.
echo.
echo Make sure you have run install.bat first!
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

echo.
echo Starting quick test...
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Test yt-dlp
echo Testing yt-dlp...
yt-dlp --version
if errorlevel 1 (
    echo ❌ yt-dlp not working
    goto :error
) else (
    echo ✅ yt-dlp working
)

REM Test Python imports
echo.
echo Testing Python imports...
python -c "import yt_dlp, whisper, google.generativeai, gtts, pydub, PyPDF2, pdfplumber; print('✅ All Python packages imported successfully')"
if errorlevel 1 (
    echo ❌ Python packages not working
    goto :error
) else (
    echo ✅ Python packages working
)

REM Test menu system
echo.
echo Testing menu system...
python -c "
import sys
sys.path.append('.')
from youtube_audio_processor import show_menu, create_folders
print('✅ Menu system working')
create_folders()
print('✅ Folder creation working')
"
if errorlevel 1 (
    echo ❌ Menu system not working
    goto :error
) else (
    echo ✅ Menu system working
)

echo.
echo ============================================
echo ✅ ALL TESTS PASSED!
echo ============================================
echo.
echo Castellanator is ready to use!
echo Run start_processor.bat to begin processing videos and PDFs.
echo.
pause
exit /b

:error
echo.
echo ❌ Some tests failed. Please run install.bat first.
echo.
pause
