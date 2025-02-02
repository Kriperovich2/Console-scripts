import os
import requests
from colorama import Fore, Style, init

# Инициализация colorama
init()

# URL репозитория
repo_url = "https://api.github.com/repos/kriperovich2/console-scripts/contents"

# Путь к папке /lsd/
download_folder = "/lsd/"

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
    print(Fore.RED + "=============================================" + Style.RESET_ALL)
    print(Fore.RED + "|          Install Best Hacking Tool          |" + Style.RESET_ALL)
    print(Fore.RED + "=============================================" + Style.RESET_ALL)
    print("\n  [ 1 ] Show all tools.")
    print("  [ x ] For Exit.")
    print(Fore.RED + "_______________________________________________" + Style.RESET_ALL)
    print(Fore.RED + "==============================================" + Style.RESET_ALL)

def fetch_sh_files():
    response = requests.get(repo_url)
    if response.status_code == 200:
        files = response.json()
        sh_files = [file for file in files if file['name'].endswith('.sh')]
        return sh_files
    else:
        print("Failed to fetch files from GitHub.")
        return []

def download_file(url, filename):
    # Проверяем, существует ли папка /lsd/, и создаем её, если нет
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Полный путь для сохранения файла
    file_path = os.path.join(download_folder, filename)
    
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
            sh_files = fetch_sh_files()
            for i, file in enumerate(sh_files):
                print(f"[ {i+1} ] {file['name']}")
            file_choice = input("Select a file to download (or 'x' to return): ")
            if file_choice.isdigit() and 0 < int(file_choice) <= len(sh_files):
                selected_file = sh_files[int(file_choice)-1]
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