@echo off
echo ============================================
echo Castellanator - Conversion History
echo ============================================
echo.
if not exist ./output (
    echo No conversions found. Run start_processor.bat first!
    pause
    exit /b
)

echo Your conversions:
echo.
for /d %%i in (../output\*) do (
    echo 📁 %%~ni
    if exist "%%i\audio.mp3" echo   🎵 audio.mp3 (English audio)
    if exist "%%i\transcript.txt" echo   📝 transcript.txt (English transcript)
    if exist "%%i\translated.txt" echo   🌍 translated.txt (Spanish translation)
    if exist "%%i\output.mp3" echo   🔊 output.mp3 (Spanish audio)
    echo.
)
echo.
echo Temporary files: ./temp/
echo.
pause
