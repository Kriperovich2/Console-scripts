#!/bin/bash

# Обновление пакетов
echo "Обновление пакетов..."
pkg update -y

# Проверка, установлен ли Python
if command -v python &> /dev/null; then
    echo "Python уже установлен, пропускаем установку."
else
    echo "Установка Python..."
    pkg install python -y
fi

# Создание файла lol.py и запись в него кода
echo "Создание файла lol.py..."
cat > lol.py <<EOF
print("Lol")
EOF

# Запуск файла lol.py
echo "Запуск файла lol.py..."
python3 lol.py