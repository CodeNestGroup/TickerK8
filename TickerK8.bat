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
python ./TickerK8_app/app_files/PYTHON/_0000_app_base.py

REM Dezaktywacja srodowiska po zakonczeniu
deactivate

pause
