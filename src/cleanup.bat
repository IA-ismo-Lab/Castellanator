@echo off
echo ============================================
echo Castellanator - Cleanup Utility
echo ============================================
echo.
echo This will remove all temporary files from temp/ folder.
echo Your output files in output/ will NOT be affected.
echo.
echo Are you sure you want to continue? (y/n):
set /p confirm=
if /i not "%confirm%"=="y" (
    echo Cleanup cancelled.
    pause
    exit /b
)

echo Cleaning up temporary files...
if exist temp\ (
    del /q temp\*.*
    echo Temporary files cleaned.
) else (
    echo No temp folder found.
)

echo.
echo Cleanup completed!
echo.
pause
