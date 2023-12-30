import subprocess
import os
choice = input("Enter 1 to download video and Enter 2 to download audio: ")
if choice == "1":
    link = input("Enter Youtube video link : ")
    os.chdir(r'C:\yt')
    command = f"yt.exe {link}"
    subprocess.run(command, shell=True)
    input("Download should be complete")
    
else:
    print("Go away demon")