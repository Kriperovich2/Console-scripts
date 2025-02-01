#!/bin/bash

# Установка Python
echo "Установка Python..."
apt install python -y

# Создание файла lol.py и запись в него кода
echo "Создание файла lol.py..."
cat > lol.py <<EOF
print("Lol")
EOF

# Запуск файла lol.py
echo "Запуск файла lol.py..."
python lol.py