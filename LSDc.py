import csv
import os
import requests
import sys
from colorama import init, Fore, Back, Style

# Инициализация colorama
init(autoreset=True)

def display_banner():
    banner = """

          .----------------.  .----------------.  .----------------.
         | .--------------. || .--------------. || .--------------. |
         | |   _____      | || |    _______   | || |  ________    | |
         | |  |_   _|     | || |   /  ___  |  | || | |_   ___ `.  | |
         | |    | |       | || |  |  (__ \_|  | || |   | |   `. \ | |
         | |    | |   _   | || |   '.___`-.   | || |   | |    | | | |
         | |   _| |__/ |  | || |  |`\____) |  | || |  _| |___.' / | |
         | |  |________|  | || |  |_______.'  | || | |________.'  | |
         | |              | || |              | || |              | |
         | '--------------' || '--------------' || '--------------' |
          '----------------'  '----------------'  '----------------'     
    """
    colored_banner = Fore.MAGENTA + banner + Fore.RESET
    print(colored_banner)


def search_in_file(filename, search_term):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if search_term in row:
                return ';'.join(row)
    return 'Information not found.'


def display_author_info():
    author_info = """
    ====================================
    |             Author               |
    |          Kriperovich2            |
    ====================================
    """
    colored_author_info = Fore.YELLOW + author_info + Fore.RESET
    print(colored_author_info)


def get_files_from_github():
    repo_url = "https://api.github.com/repos/kriperovich2/LSD-SCRIPT-db/contents/"
    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            files = [item['name'] for item in response.json() if item['type'] == 'file']
            return files
        else:
            print(Fore.RED + "Failed to fetch files from GitHub." + Fore.RESET)
            return []
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Fore.RESET)
        return []


def download_file(file_name):
    base_url = "https://raw.githubusercontent.com/kriperovich2/LSD-SCRIPT-db/main/"
    url = base_url + file_name

    # Проверяем, существует ли папка 'lsd'
    download_dir = 'lsd' if os.path.exists('lsd') else '.'
    file_path = os.path.join(download_dir, file_name)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(Fore.GREEN + f"File {file_name} downloaded successfully to {download_dir}." + Fore.RESET)
            restart_script()
        else:
            print(Fore.RED + f"File {file_name} not found on GitHub." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Fore.RESET)


def restart_script():
    print(Fore.CYAN + "Restarting the script..." + Fore.RESET)
    os.execv(sys.executable, ['python'] + sys.argv)


def main():
    # Print the current working directory for verification
    print(Fore.BLUE + "Current working directory:", os.getcwd() + Fore.RESET)

    # Specify the full path to your file if it is not in the current working directory
    filename = 'yandex_eda.csv'

    while True:
        display_banner()
        menu = """
                                 Main menu

          ╔════════════════════╗           ╔════════════════════╗
          ║ [1] Download       ║           ║ [2] Comming soon.. ║
          ╚════════════════════╝           ╚════════════════════╝
          ╔════════════════════╗           ╔════════════════════╗
          ║ [3] Comming soon.. ║           ║ [4] Exit           ║
          ╚════════════════════╝           ╚════════════════════╝
                           ╔═══════════════════╗
                           ║     [5] Author    ║
                           ╚═══════════════════╝
        """
        colored_menu = Fore.BLUE + menu + Fore.RESET
        print(colored_menu)

        choice = input(Fore.GREEN + "Select an option: " + Fore.RESET).strip()

        if choice == '1':
            files = get_files_from_github()
            if files:
                print(Fore.CYAN + "\nAvailable files:" + Fore.RESET)
                for i, file in enumerate(files, start=1):
                    print(f"{i}. {file}")
                file_number = input(Fore.GREEN + "Enter the file number to download: " + Fore.RESET).strip()
                try:
                    file_number = int(file_number)
                    if 1 <= file_number <= len(files):
                        download_file(files[file_number - 1])
                    else:
                        print(Fore.RED + "Invalid file number." + Fore.RESET)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number." + Fore.RESET)
            else:
                print(Fore.RED + "No files found in the repository." + Fore.RESET)
        elif choice == '2':
            print(Fore.YELLOW + "Exiting the program." + Fore.RESET)
            exit()
        elif choice == '3':
            print(Fore.YELLOW + "Exiting the program." + Fore.RESET)
            exit()
        elif choice == '4':
            print(Fore.YELLOW + "Exiting the program." + Fore.RESET)
            break
        elif choice == '5':
            display_author_info()
        else:
            print(Fore.RED + "Invalid choice. Please enter '1', '2', '3', '4' or '5'." + Fore.RESET)

        # Wait for Enter before returning to the menu
        input(Fore.CYAN + "\nPress Enter to continue..." + Fore.RESET)


if __name__ == "__main__":
    main()
