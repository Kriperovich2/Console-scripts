import os
import requests
from colorama import Fore, Style, init

# Инициализация colorama
init()

# Правильный URL репозитория
repo_url = "https://api.github.com/repos/Kriperovich2/LSD-SCRIPT-DB/contents"

# Путь к папке lsd (если папка существует, файлы будут сохраняться туда)
download_folder = "lsd"

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + """
         ,.  '                    ,. -,        ;'*¨'`·- .,  ‘            
       /   ';\              ,.·'´,    ,'\       \`:·-,. ,   '` ·.  '      
     ,'   ,'::'\         ,·'´ .·´'´-·'´::::\'      '\:/   ;\:'`:·,  '`·, '   
    ,'    ;:::';'       ;    ';:::\::\::;:'        ;   ;'::\;::::';   ;\   
    ';   ,':::;'        \·.    `·;:'-·'´           ;  ,':::;  `·:;;  ,':'\' 
    ;  ,':::;' '         \:`·.   '`·,  '          ;   ;:::;    ,·' ,·':::; 
   ,'  ,'::;'              `·:'`·,   \'           ;  ;:::;'  ,.'´,·´:::::; 
   ;  ';_:,.-·'´';\‘        ,.'-:;'  ,·\         ':,·:;::-·´,.·´\:::::;´'  
   ',   _,.-·'´:\:\‘  ,·'´     ,.·´:::'\         \::;. -·´:::::;\;·´     
    \¨:::::::::::\';   \`*'´\::::::::;·'‘         \;'\::::::::;·´'        
     '\;::_;:-·'´‘      \::::\:;:·´                 `\;::-·´            
       '¨                 '`*'´‘                                         
    """ + Style.RESET_ALL)
    print(Fore.RED + "           =============================================" + Style.RESET_ALL)
    print(Fore.RED + "           |         Install Best Hacking Tool         |" + Style.RESET_ALL)
    print(Fore.RED + "           =============================================" + Style.RESET_ALL)
    print("\n  [ 1 ] Show all files.")
    print("  [ x ] For Exit.")
    print(Fore.RED + "_______________________________________________" + Style.RESET_ALL)
    print(Fore.RED + "==============================================" + Style.RESET_ALL)

def fetch_files():
    response = requests.get(repo_url)
    if response.status_code == 200:
        files = response.json()
        # Фильтруем только файлы (исключаем папки)
        files_only = [file for file in files if file['type'] == 'file']
        return files_only
    else:
        print("Failed to fetch files from GitHub.")
        return []

def download_file(url, filename):
    # Если папка /lsd существует, сохраняем файл туда
    if os.path.exists(download_folder):
        file_path = os.path.join(download_folder, filename)
    else:
        # Иначе сохраняем файл в текущую директорию
        file_path = filename
    
    # Скачиваем файл
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"File saved to {file_path}")
    else:
        print("Failed to download the file.")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            files = fetch_files()
            for i, file in enumerate(files):
                print(f"[ {i+1} ] {file['name']}")
            file_choice = input("Select a file to download (or 'x' to return): ")
            if file_choice.isdigit() and 0 < int(file_choice) <= len(files):
                selected_file = files[int(file_choice)-1]
                download_file(selected_file['download_url'], selected_file['name'])
            elif file_choice.lower() == 'x':
                continue
            else:
                print("Invalid choice.")
        elif choice.lower() == 'x':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
