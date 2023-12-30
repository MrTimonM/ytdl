import subprocess
import os
from colorama import Fore, Style, init

init(autoreset=True)
print(Fore.BLUE + "Welcome to Youtube Donwloader v4.0" + Style.RESET_ALL)
while True:
    print(Fore.MAGENTA + "1.Download video from Youtube" + Style.RESET_ALL)
    print(Fore.MAGENTA + "2.Download Audio from Youtube" + Style.RESET_ALL)
    print(Fore.MAGENTA + "3.Download from Playlist (Audio-Only)" + Style.RESET_ALL)
    print(Fore.MAGENTA + "4.Exit the program" + Style.RESET_ALL)
    choice = input(Fore.YELLOW + "Enter Your choice : " + Style.RESET_ALL)
    if choice == "1":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube video link: " + Style.RESET_ALL)
        command = f"yt.exe {link}"
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Deleting original file" in output:
            print(Fore.GREEN + "Audio download Successful\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed\n" + Style.RESET_ALL)
        continue
    
    elif choice =="2":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube video link: " + Style.RESET_ALL)
        command = f"yt.exe -x --audio-format mp3 {link}"
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Deleting original file" in output:
            print(Fore.GREEN + "Audio download Successful\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed\n" + Style.RESET_ALL)
        continue
    
    elif choice =="3":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube Playlist link: " + Style.RESET_ALL)
        command = f'yt.exe --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {link}'
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Deleting original file" in output:
            print(Fore.GREEN + "Audio Playlist download Successful\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed\n" + Style.RESET_ALL)
        continue
    
    elif choice =="4":
        os.chdir(r"c:\yt")
        link = input(Fore.CYAN + "Enter Youtube Playlist link: " + Style.RESET_ALL)
        command= f"yt.exe -i -f mp4 --yes-playlist {link}"
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Finished downloading playlist" in output:
            print(Fore.GREEN + "Audio download Successful\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed\n" + Style.RESET_ALL)
        continue
    elif choice == "5":
        break;
    else:
        print(Fore.RED + "Invalid input.\n"+ Style.RESET_ALL)

input(Fore.GREEN + "Enter any key to exit" + Style.RESET_ALL)
        
    
    