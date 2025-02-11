import os
import requests
from colorama import Fore, Style, init

# Инициализация colorama
init()

# URL репозитория
repo_url = "https://api.github.com/repos/Kriperovich2/lsd-script/contents"

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + r"""
         ,.  '                    ,. -,        ;'*¨'·- .,  ‘            
       /   ';\              ,.·'´,    ,'\       \:·-,. ,   ' ·.  '      
     ,'   ,'::'\         ,·'´ .·´'´-·'´::::\'      '\:/   ;\:':·,  '·, '   
    ,'    ;:::';'       ;    ';:::\::\::;:'        ;   ;'::\;::::';   ;\   
    ';   ,':::;'        \·.    ·;:'-·'´           ;  ,':::;  ·:;;  ,':'\' 
    ;  ,':::;' '         \:·.   '·,  '          ;   ;:::;    ,·' ,·':::; 
   ,'  ,'::;'              ·:'·,   \'           ;  ;:::;'  ,.'´,·´:::::; 
   ;  ';_:,.-·'´';\‘        ,.'-:;'  ,·\         ':,·:;::-·´,.·´\:::::;´'  
   ',   _,.-·'´:\:\‘  ,·'´     ,.·´:::'\         \::;. -·´:::::;\;·´     
    \¨:::::::::::\';   \*'´\::::::::;·'‘         \;'\::::::::;·´'        
     '\;::_;:-·'´‘      \::::\:;:·´                 \;::-·´            
       '¨                 '*'´‘                                         
    """ + Style.RESET_ALL)
    print(Fore.RED + "=============================================" + Style.RESET_ALL)
    print(Fore.RED + "|          Install Best Hacking Tool          |" + Style.RESET_ALL)
    print(Fore.RED + "=============================================" + Style.RESET_ALL)
    print("\n  [ 1 ] SOFT")
    print("  [ 2 ] DB")
    print("  [ X ] EXIT")
    print(Fore.RED + "___________" + Style.RESET_ALL)
    print(Fore.RED + "==============================================" + Style.RESET_ALL)

def fetch_files():
    response = requests.get(repo_url)
    if response.status_code == 200:
        files = response.json()
        return files
    else:
        print("Failed to fetch files from GitHub.")
        return []

def download_file(url, filename):
    # Скачиваем файл
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File saved to {filename}")
    else:
        print("Failed to download the file.")

def download_soft_files():
    files = fetch_files()
    for file in files:
        if file['type'] == 'file' and not file['name'].startswith('DB'):
            print(f"Downloading {file['name']}...")
            download_file(file['download_url'], file['name'])

def download_db_files():
    files = fetch_files()
    for file in files:
        if file['type'] == 'file' and file['name'].startswith('DB'):
            print(f"Downloading {file['name']}...")
            download_file(file['download_url'], file['name'])

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == '1':
            download_soft_files()
        elif choice == '2':
            download_db_files()
        elif choice == 'x':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if name == "main":
    main()
