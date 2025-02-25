@echo off
cd /d "%~dp0"

REM Sprawdzenie czy katalog .venv istnieje
if not exist .venv (
    echo Tworzenie srodowiska wirtualnego...
    python -m venv .venv
)

REM Aktywacja srodowiska wirtualnego
call .venv\Scripts\activate

REM Uruchomienie skryptu Python
python ./TickerK8_updater/_00_main.py

REM Dezaktywacja srodowiska po zakonczeniu
deactivate

pause
