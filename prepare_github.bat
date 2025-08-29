@echo off
echo ============================================
echo Castellanator - GitHub Preparation
echo ============================================
echo.
echo This script will prepare your Castellanator project
echo for GitHub publication.
echo.
echo Press any key to continue...
pause >nul

echo.
echo Step 1: Creating Git repository...
if not exist .git (
    git init
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

echo.
echo Step 2: Adding all files to Git...
git add .
echo ✅ Files staged for commit

echo.
echo Step 3: Creating initial commit...
git commit -m "Initial commit: Castellanator - AI-Powered Content Translator

🎧 Professional AI application for YouTube and PDF processing
- YouTube video to Spanish audio conversion
- PDF document to Spanish audio conversion
- Interactive menu system
- Automated installation and testing
- Professional project structure

Features:
✅ AI-powered transcription (Whisper)
✅ Professional translation (Gemini AI)
✅ Natural voice synthesis (Google TTS)
✅ Smart chunking for long content
✅ Organized output management
✅ Cross-platform compatibility

Made with ❤️ by IA-ismo LAB"
echo ✅ Initial commit created

echo.
echo Step 4: Setting up GitHub remote...
echo.
echo 📋 Next steps for GitHub:
echo 1. Create a new repository on GitHub.com
echo 2. Copy the repository URL
echo 3. Run: git remote add origin YOUR_REPO_URL
echo 4. Run: git push -u origin main
echo.
echo Or use GitHub CLI if installed:
echo gh repo create castellanator --public --source=. --push
echo.

echo ============================================
echo ✅ GitHub preparation complete!
echo ============================================
echo.
echo Your Castellanator project is ready for GitHub!
echo.
pause
