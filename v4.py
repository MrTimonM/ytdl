import subprocess
import os
from colorama import Fore, Style, init

init(autoreset=True)
print(Fore.BLUE + "Welcome to Youtube Donwloader v4.0" + Style.RESET_ALL)
while True:
    choice = input(Fore.GREEN + "1.Download video from Youtube\n2.Download Audio from Youtube\n3.Download from Playlist (Audio-Only)\n4.Exit the program\nEnter Your choice: ")
    if choice == "1":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube video link: " + Style.RESET_ALL)
        command = f"yt.exe {link}"
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Deleting original file" in output:
            print(Fore.GREEN + "Audio download Successful" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed" + Style.RESET_ALL)
        continue
    
    
    elif choice =="2":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube video link: " + Style.RESET_ALL)
        command = f"yt.exe -x --audio-format mp3 {link}"
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Deleting original file" in output:
            print(Fore.GREEN + "Audio download Successful" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed" + Style.RESET_ALL)
        continue
    
    elif choice =="3":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube Playlist link: " + Style.RESET_ALL)
        command = f'yt.exe --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {link}'
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Deleting original file" in output:
            print(Fore.GREEN + "Audio Playlist download Successful" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed" + Style.RESET_ALL)
        continue
    
    
    elif choice == "4":
        break;
    else:
        print(Fore.RED + "Invalid input."+ Style.RESET_ALL)

input(Fore.YELLOW + "Enter any key to exit" + Style.RESET_ALL)
        
    
    