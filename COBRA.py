import os
import time
import platform
os.system("clear")
os.system("xdg-open https://www.facebook.com/groups/1354738058401296/?ref=share&mibextid=NSMWB")
print("\n\033[38;5;195m[\033[38;5;46m+\033[38;5;195m]\033[38;5;46m CHECKING UPDATE 💚")
time.sleep(2)
os.system("git pull")
time.sleep(1)
bit = platform.architecture()[0]
if bit=='64bit':
    print("[+] CONGRATULATION YOU DEVICE SUPPORT THIS TOOLS ")
    time.sleep(1)
    import green