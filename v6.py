import subprocess
import os
from colorama import init, Style, Fore

init(autoreset=True)

print(Fore.BLACK + "Welcome to YT downloader V6.0" + Style.RESET_ALL)
while True:
    print(Fore.MAGENTA + "1. Download video " + Style.RESET_ALL)
    print(Fore.MAGENTA + "2. Download Audio " + Style.RESET_ALL)
    print(Fore.MAGENTA + "3. Download Video playlist " + Style.RESET_ALL)
    print(Fore.MAGENTA + "4. Download Audio playlist " + Style.RESET_ALL)
    print(Fore.MAGENTA + "5. Cut downloaded Video " + Style.RESET_ALL)
    print(Fore.MAGENTA + "6. Cut downloaded Audio " + Style.RESET_ALL)
    choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)
    if choice == "1":
        os.chdir(r"c:\yt")
        link = input(Fore.BLUE + "Enter Youtube Video Link: " + Style.RESET_ALL)
        command = f"yt.exe {link}"
        result = subprocess.run(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        final = (result.stdout + result.stderr).decode('utf-8')
        if "Deleting original file" in final:
            print(Fore.GREEN + "Download Successful" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Download Failed" + Style.RESET_ALL)
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
        command= f"yt.exe -i -f mp4 --yes-playlist {link}"
        print(Fore.YELLOW + "Waiting for the download to complete..." + Style.RESET_ALL)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = (result.stdout + result.stderr).decode('utf-8')
        
        if "Finished downloading playlist" in output:
            print(Fore.GREEN + "Playlist download Successful\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Download failed\n" + Style.RESET_ALL)
        continue

    elif choice =="4":
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

