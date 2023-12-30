import subprocess
import os
from colorama import Fore, Style, init

init(autoreset=True)
print(Fore.BLUE + "Welcome to Youtube Downloader v4.0" + Style.RESET_ALL)

while True:
    choice = input(Fore.GREEN + "1. Download video from Youtube\n2. Download Audio from Youtube\n3. Download from Playlist (Audio-Only)\n4. Exit the program\nEnter Your choice: ")

    if choice == "1":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube video link: " + Style.RESET_ALL)
        command = f"yt.exe {link}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')  # Decode bytes to string
        print(Fore.BLUE + "Output:", output + Style.RESET_ALL)
        if result.returncode == 0:
            print(Fore.GREEN + "Download Successful" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed" + Style.RESET_ALL)
        continue

    elif choice == "2":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube video link: " + Style.RESET_ALL)
        command = f"yt.exe -x --audio-format mp3 {link}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')  # Decode bytes to string
        print(Fore.BLUE + "Output:", output + Style.RESET_ALL)
        if result.returncode == 0:
            print(Fore.GREEN + "Download Successful" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed" + Style.RESET_ALL)
        continue

    elif choice == "3":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube Playlist link: " + Style.RESET_ALL)
        command = f'yt.exe --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {link}'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')  # Decode bytes to string
        print(Fore.BLUE + "Output:", output + Style.RESET_ALL)
        if result.returncode == 0:
            print(Fore.GREEN + "Playlist download Successful" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed" + Style.RESET_ALL)
        continue

    elif choice == "4":
        break

    else:
        print(Fore.RED + "Invalid input." + Style.RESET_ALL)

input(Fore.YELLOW + "Enter any key to exit" + Style.RESET_ALL)
