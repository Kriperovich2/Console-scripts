#!/bin/bash

# Установка Python (если не установлен)
if ! command -v python3 &> /dev/null
then
    echo "Python3 не установлен. Устанавливаем..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# Скачивание файла из GitHub
GITHUB_REPO="https://raw.githubusercontent.com/kriperovich2/console-scripts/main/private/snos.py"
FILE_NAME="snos.py"

echo "Скачивание файла $FILE_NAME из GitHub..."
curl -O $GITHUB_REPO

# Проверка, скачался ли файл
if [ ! -f "$FILE_NAME" ]; then
    echo "Ошибка: файл $FILE_NAME не скачан."
    exit 1
fi

# Установка недостающих библиотек
echo "Установка недостающих библиотек..."
pip3 install -r <(grep -oP '^\s*import\s+\K\w+' $FILE_NAME | awk '{print $1}' | xargs -I {} echo "{}")

# Запуск файла
echo "Запуск файла $FILE_NAME..."
python3 $FILE_NAME