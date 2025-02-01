#!/bin/bash

# Функция для проверки установки пакета
is_installed() {
    command -v $1 &> /dev/null
}

# Обновление пакетов
echo "Обновление пакетов..."
apt update -y

# Проверка и установка Python
if is_installed python; then
    echo "Python уже установлен."
else
    echo "Установка Python..."
    apt install python -y
fi

# Проверка и установка OpenSSL
if is_installed openssl; then
    echo "OpenSSL уже установлен."
else
    echo "Установка OpenSSL..."
    apt install openssl -y
fi

# Проверка и установка libssl-dev
if dpkg -l | grep -q libssl-dev; then
    echo "libssl-dev уже установлен."
else
    echo "Установка libssl-dev..."
    apt install libssl-dev -y
fi

# Проверка и установка python-dev
if dpkg -l | grep -q python-dev; then
    echo "python-dev уже установлен."
else
    echo "Установка python-dev..."
    apt install python-dev -y
fi

# Проверка и переустановка pip с поддержкой SSL
if is_installed pip; then
    echo "pip уже установлен."
else
    echo "Установка pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --force-reinstall
fi

# Проверка и установка библиотеки termcolor
if python -c "import termcolor" &> /dev/null; then
    echo "Библиотека termcolor уже установлена."
else
    echo "Установка библиотеки termcolor..."
    pip install termcolor
fi

# Создание файла rainbow_text.py
echo "Создание файла rainbow_text.py..."
cat > rainbow_text.py <<EOF
import sys
from termcolor import colored

# Функция для создания радужного текста
def rainbow_text(text):
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    rainbow_text = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        rainbow_text += colored(char, color)
    return rainbow_text

# Основная логика
if __name__ == "__main__":
    print("Введите текст (для выхода введите 'exit'):")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Выход из программы.")
            break
        print(rainbow_text(user_input))
EOF

# Запуск Python-скрипта
echo "Запуск программы..."
python rainbow_text.py