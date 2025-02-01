#!/bin/bash

# Обновление пакетов
echo "Обновление пакетов..."
apt update -y

# Установка Python
echo "Установка Python..."
apt install python -y

# Установка pip (если не установлен)
echo "Установка pip..."
apt install python-pip -y

# Установка библиотеки termcolor
echo "Установка библиотеки termcolor..."
pip install termcolor

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