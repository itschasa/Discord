# -*- coding: utf-8 -*-
import re
from colorama import Fore, init
import requests
import json
from lxml.html import fromstring
import traceback
import random
import ctypes
import string
import os
import base64
import subprocess
import time
import threading
import sys

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTCYAN_EX
dblue = Fore.CYAN
gray = Fore.LIGHTBLACK_EX

fail = 0
success = 0
checked = 0
proxy_changes = 0
proxy_down = 0

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)

def get_id():
    if 'nt' in os.name: 
        p = subprocess.Popen("wmic csproduct get uuid", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1].strip("  \r\r")
    else:
        return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())

def proxy_gen():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    f = open("proxies.txt", "w")
    for i in parser.xpath('//tbody/tr')[:100]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            f.write(f"{proxy}\n")
            print(f"{gray}[{green}+{gray}]{white} {proxy}")
    r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&ssl=yes")
    for x in r.text.split("\n"):
        print(f"{gray}[{green}+{gray}]{white} {x}")
        f.write(f"{x}")
    f.close()

def nitro_codes(amount):
    #print(f"{gray}[{green}+{gray}]{white} https://discord.gift/{randomCode}")
    try:
        open("gifts.txt", "x").close()
    except:
        print(f"{gray}[{yellow}!{gray}]{white} gifts.txt already exists, delete it before continuing.")
    else:
        f = open("gifts.txt", "w")
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        for x in range(amount):
            randomCode = ""
            for y in range(16):
                randomCode += random.choice(letters)
            if x == (amount - 1):
                f.write(f"https://discord.gift/{randomCode}")
            else:
                f.write(f"https://discord.gift/{randomCode}\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Generator] Discord Gifts: {x + 1}")
            print(f"{gray}[{green}+{gray}]{white} https://discord.gift/{randomCode}")
        f.close()
        print(f"{gray}[{yellow}!{gray}]{white} Saved {amount} codes in gifts.txt.")

def discord_tokens(amount):
    count = 0
    f = open("tokens.txt", "w")
    for x in range(amount):
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(random.randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                        for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            f.write(f"{token}\n")
            print(f"{gray}[{green}+{gray}]{white} {token}")
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Generator] Discord Tokens: {x + 1}")
    f.close()

while True:
    title("[Generator] Main Menu")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"""{blue}
                                    _              
                                   ( )_            
   __    __   ___    __  _ __   _ _|  _)  _   _ __ 
 / _  \/ __ \  _  \/ __ \  __)/ _  ) |  / _ \(  __)
( (_) |  ___/ ( ) |  ___/ |  ( (_| | |_( (_) ) |   
 \__  |\____)_) (_)\____)_)   \__ _)\__)\___/(_)   
( )_) |                                            
 \___/                                             

{gray}[{blue}1{gray}]{white} Proxies
{gray}[{blue}2{gray}]{white} Discord Gifts
{gray}[{blue}3{gray}]{white} Discord Tokens
 """)
    print(f"{blue}>> {white}", end='')
    choice = input()
    if choice == "1":
        title("[Generator] Proxies")
        proxy_gen()
        print(f"{gray}[{yellow}!{gray}]{white} Saved to proxies.txt.")
        time.sleep(2)
    elif choice == "2":
        title("[Generator] Discord Gifts")
        print(f"{blue}>> {white}Amount: ", end='')
        try:
            amount = int(input())
        except:
            print(f"{gray}[{red}-{gray}]{white} Not an integer.")
        else:
            nitro_codes(amount)
            time.sleep(2)
    elif choice == "3":
        title("[Generator] Discord Tokens")
        print(f"{blue}>> {white}Amount: ", end='')
        try:
            amount = int(input())
        except:
            print(f"{gray}[{red}-{gray}]{white} Not an integer.")
        else:
            discord_tokens(amount)
            print(f"{gray}[{yellow}!{gray}]{white} Saved to discord_tokens.txt.")
        time.sleep(2)
    else:
        title("[Generator] Invalid Option")
        print(f"{gray}[{red}-{gray}]{white} Not an Option.")
        time.sleep(1)