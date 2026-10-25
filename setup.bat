@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Building local virtual environment...
    py -m venv .venv
    if errorlevel 1 exit /b 1
)

echo Installing essential tracking packages...
.venv\Scripts\pip.exe install -r requirements.txt

echo Booting Nova Voice Assistant...
.venv\Scripts\python.exe nova_assistant.py
pause
