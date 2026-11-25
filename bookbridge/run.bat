@echo off
title BookBridge - Vivekananda Institute of Professional Studies
color 0b

echo =====================================================================
echo    BookBridge - Campus Book and Learning-Material Exchange Board
echo           VIVEKANANDA INSTITUTE OF PROFESSIONAL STUDIES
echo =====================================================================
echo Campus: Pitampura, New Delhi ^| Affiliated to GGSIPU, Delhi
echo =====================================================================
echo.

cd /d "%~dp0"

echo [1/3] Ensuring SQLite database initialization...
python database.py

echo.
echo [2/3] Launching BookBridge Web Portal on http://127.0.0.1:5000...
start "" http://127.0.0.1:5000

echo.
echo [3/3] Starting Web Server (Press Ctrl+C to stop)...
echo.
python app.py

pause
