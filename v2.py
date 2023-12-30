import subprocess
import os
print("Youtube downloader using YT-DL")
choice = input("Enter 1 to download video and enter 2 to download audio: ")

if choice == "1":
    link = input("Enter youtube video link: ")
    command = f"yt.exe link"
    os.chdir(r"c:\yt")
    subprocess.run(command, shell=True)
    print("download complete :D")
    input("Enter any key to exit")
    
elif choice == "2":
    link = input("Enter youtube video link: ")
    os.chdir(r"c:\yt")
    command  = f"yt.exe -x --audio-format mp3 {link}"
    subprocess.run(command, shell=True)
    print("download complete :D")
    input("Enter any key to exit")