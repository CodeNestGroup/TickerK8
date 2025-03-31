#!/bin/bash

# Funkcja, która sprawdza, czy jesteśmy na systemie Windows
is_windows() {
    [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]
}

# Ustalanie katalogu głównego projektu
PROJECT_DIR="$(dirname "$(realpath "$0")")"
VENV_DIR="$PROJECT_DIR/.venv"

# Wyświetlenie wartości PROJECT_DIR dla celów debugowania
echo "PROJECT_DIR: $PROJECT_DIR"

# Sprawdzenie, czy katalog TickerK8_updater istnieje
if [ ! -d "$PROJECT_DIR/TickerK8_updater" ]; then
    echo "Nie znaleziono katalogu TickerK8_updater w $PROJECT_DIR. Upewnij się, że skrypt jest uruchamiany z katalogu projektu."
    exit 1
fi

# Sprawdzenie, czy wirtualne środowisko istnieje
if [ ! -d "$VENV_DIR" ]; then
    echo "Nie znaleziono wirtualnego środowiska. Upewnij się, że zostało ono utworzone."
    exit 1
fi

# Aktywacja wirtualnego środowiska zależnie od systemu operacyjnego
if is_windows; then
    # Windows
    source "$VENV_DIR/Scripts/activate"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    source "$VENV_DIR/bin/activate"
else
    # Linux (lub inne systemy UNIX-owe)
    source "$VENV_DIR/bin/activate"
fi

# Uruchomienie głównego pliku aplikacji Python
python "$PROJECT_DIR/TickerK8_updater/APP_FILES/PYTHON/_00_main.py"
