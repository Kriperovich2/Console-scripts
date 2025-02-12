import csv
import os
import requests
import sys
from pystyle import Colors, Box, Write, Center, Colorate


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
    colored_banner = Colorate.Vertical(Colors.purple_to_red, Center.XCenter(banner))
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
    |            Author                |
    |         Kriperovich2             |
    ====================================
    """
    colored_author_info = Colorate.Vertical(Colors.yellow_to_red, Center.XCenter(author_info))
    print(colored_author_info)


def get_files_from_github():
    repo_url = "https://api.github.com/repos/kriperovich2/LSD-SCRIPT-db/contents/"
    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            files = [item['name'] for item in response.json() if item['type'] == 'file']
            return files
        else:
            print("Failed to fetch files from GitHub.")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
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
            print(f"File {file_name} downloaded successfully to {download_dir}.")
            restart_script()
        else:
            print(f"File {file_name} not found on GitHub.")
    except Exception as e:
        print(f"An error occurred: {e}")


def restart_script():
    print("Restarting the script...")
    os.execv(sys.executable, ['python'] + sys.argv)


def main():
    # Print the current working directory for verification
    print("Current working directory:", os.getcwd())

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
        colored_menu = Colorate.Vertical(Colors.blue_to_green, Center.XCenter(menu))
        print(colored_menu)

        choice = input("Select an option: ").strip()

        if choice == '1':
            files = get_files_from_github()
            if files:
                print("\nAvailable files:")
                for i, file in enumerate(files, start=1):
                    print(f"{i}. {file}")
                file_number = input("Enter the file number to download: ").strip()
                try:
                    file_number = int(file_number)
                    if 1 <= file_number <= len(files):
                        download_file(files[file_number - 1])
                    else:
                        print("Invalid file number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No files found in the repository.")
        elif choice == '2':
            print("Exiting the program.")
            exit()
        elif choice == '3':
            print("Exiting the program.")
            exit()
        elif choice == '4':
            print("Exiting the program.")
            break
        elif choice == '5':
            display_author_info()
        else:
            print("Invalid choice. Please enter '1', '2', '3', '4' or '5'.")

        # Wait for Enter before returning to the menu
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()