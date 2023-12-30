import subprocess
import os
choice = input("Enter 1 for video and Enter 2 for Audio: ")

if choice =="1":
    os.chdir(r"C:\yt")
    link = input("Enter link: ")
    command= f"yt.exe -i -f mp4 --yes-playlist {link}"
    subprocess.run(command, shell=True)
    print("Download should be complete")
    
    
    
else:
    print("go away demon")