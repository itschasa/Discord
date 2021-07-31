# -*- coding: utf-8 -*-
import subprocess
import os
from colorama import Fore, init
import ctypes
import time
import threading

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTCYAN_EX
dblue = Fore.CYAN
gray = Fore.LIGHTBLACK_EX

def get_id():
    if 'nt' in os.name: 
        p = subprocess.Popen("wmic csproduct get uuid", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1].strip("  \r\r")
    else:
        return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)
headers = { 
    "Content-Type": "application/json", 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

cwd = os.getcwd()


def openbb(c):
    subprocess.call(f'{c}', creationflags=subprocess.CREATE_NEW_CONSOLE)

while True:
    title("[BlueBot] Main Menu")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"""
{blue}                                        _     _               _           _   
{blue}                                       ( )   (_ )            ( )         ( )_ 
{blue}                                       | |_   | | _   _   __ | |_     _  |  _)
{blue}                                       |  _ \ | |( ) ( )/ __ \  _ \ / _ \| |  
{blue}                                       | |_) )| || (_) |  ___/ |_) ) (_) ) |_ 
{blue}                                       (_ __/(___)\___/ \____)_ __/ \___/ \__)                  

{dblue}                             ╔═════════════════════════════╦════════════════════════════╗
{dblue}                             ║ {gray}[{green}1{gray}] {white}BotNuker                {dblue}║ {gray}[{green}2{gray}] {white}Sniffer                {dblue}║
{dblue}                             ║ {gray}[{green}3{gray}] {white}Generator               {dblue}║ {gray}[{green} {gray}] {white}                       {dblue}║
{dblue}                             ╚═════════════════════════════╩════════════════════════════╝
""")

    print(f"\n\n\n\n\n\n{blue}                                                         >> {white}", end='')
    try:
        choice = int(input())
    except:
        print(f"\n                                                 {gray}[{red}!{gray}]{white} Invalid Choice.")
        time.sleep(1)
    else:
        if choice == 1:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading BotNuker...")
            time.sleep(0.7)
            try:
                mydir = cwd + "\\BotNuker"
                mydir_new = os.chdir(mydir)
                threading.Thread(target=openbb, args=(f'{cwd}\BotNuker\BotNuker.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        elif choice == 2:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading Sniffer...")
            time.sleep(0.7)
            try:
                mydir = cwd + "\\Sniffer"
                os.chdir(mydir)
                threading.Thread(target=openbb, args=(f'{cwd}\Sniffer\Sniffer.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        elif choice == 3:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading Generator...")
            time.sleep(0.7)
            try:
                mydir = cwd + "\\Generator"
                mydir_new = os.chdir(mydir)
                threading.Thread(target=openbb, args=(f'{cwd}\Generator\Generator.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        else:
            print(f"                                                   {gray}[{red}!{gray}]{white} Invalid Choice.")
        time.sleep(1)
