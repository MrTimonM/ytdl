import subprocess
import os
from colorama import init, Fore, Style

init(autoreset=True)

while True:
    choice = input(Fore.GREEN + "Enter 1 to download video and Enter 2 to download audio and enter q to exit: " + Style.RESET_ALL)
    if choice == "q":
        break
    link = input(Fore.CYAN + "Enter youtube video link: "+ Style.RESET_ALL)
    os.chdir(r"c:\yt")
    if choice == "1":
        command = f"yt.exe {link}"
        
    elif choice == "2":
        command = f"yt.exe -x --audio-format mp3 {link}"
        
    else:
        print(Fore.RED + "Invalid choice" + Style.RESET_ALL)
        continue
    subprocess.run(command, shell = True)
    print(Fore.YELLOW + "Download complete" + Style.RESET_ALL)
input(Fore.MAGENTA + "Enter any key to exit" + Style.RESET_ALL)