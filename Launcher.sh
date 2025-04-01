#!/bin/bash

# Sprawdzenie systemu operacyjnego
is_windows() {
    case "$(uname -s)" in
        MINGW*|MSYS*|CYGWIN*) return 0 ;; # Windows
        *) return 1 ;;
    esac
}

# Ustalanie katalogu głównego projektu
PROJECT_DIR="$(cd "$(dirname "$0")"; pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

echo "PROJECT_DIR: $PROJECT_DIR"

# Sprawdzenie, czy Python jest zainstalowany
if ! command -v python3 &> /dev/null; then
    echo "Python3 nie jest zainstalowany. Pobieranie wersji portable..."
    if is_windows; then
        curl -o python.zip https://www.python.org/ftp/python/3.11.4/python-3.11.4-embed-amd64.zip
        unzip python.zip -d "$PROJECT_DIR/python"
        PYTHON_EXEC="$PROJECT_DIR/python/python.exe"
    else
        curl -o python.tar.gz https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz
        tar -xzf python.tar.gz -C "$PROJECT_DIR"
        PYTHON_EXEC="$PROJECT_DIR/python/bin/python3"
    fi
else
    PYTHON_EXEC="python3"
fi

# Tworzenie wirtualnego środowiska, jeśli nie istnieje
if [ ! -d "$VENV_DIR" ]; then
    echo "Tworzenie wirtualnego środowiska..."
    $PYTHON_EXEC -m venv "$VENV_DIR"
fi

# Aktywacja środowiska
if is_windows; then
    source "$VENV_DIR/Scripts/activate"
else
    source "$VENV_DIR/bin/activate"
fi

# Instalacja zależności
pip install --upgrade pip
pip install -r "$PROJECT_DIR/TickerK8_updater/APP_FILES/CONFIG/requirements.txt"

# Uruchomienie aplikacji
python "$PROJECT_DIR/TickerK8_updater/APP_FILES/PYTHON/_00_main.py"
