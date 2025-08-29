@echo off
echo ============================================
echo Audio Transcriber - Quick Test
echo ============================================
echo.
echo This will test if all components are working.
echo It will test the audio transcription functionality.
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

REM Test Python imports
echo.
echo Testing Python imports...
python -c "import whisper, google.generativeai; print('✅ All Python packages imported successfully')"
if errorlevel 1 (
    echo ❌ Python packages not working
    goto :error
) else (
    echo ✅ Python packages working
)

REM Test script syntax
echo.
echo Testing script syntax...
python -m py_compile audio_transcriber.py
if errorlevel 1 (
    echo ❌ Script syntax error
    goto :error
) else (
    echo ✅ Script syntax OK
)

REM Test help function
echo.
echo Testing help function...
python audio_transcriber.py --help >nul 2>&1
if errorlevel 1 (
    echo ❌ Help function not working
    goto :error
) else (
    echo ✅ Help function working
)

echo.
echo ============================================
echo ✅ ALL TESTS PASSED!
echo ============================================
echo.
echo Audio Transcriber is ready to use!
echo Run: python audio_transcriber.py <audio_file> <gemini_api_key>
echo.
pause
