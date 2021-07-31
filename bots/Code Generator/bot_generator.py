# Config
# If you know what your doing, feel free to edit the code.

# Bot Token
# Token of the Bot which you want to use.
TOKEN = ""

# Log File
# Where all the logs of everything are stored.
# Default: "logs.txt"
LOG_FILE = "logs.txt"
# File where the codes are stored.
# Codes are given out by lines, so make sure they are split line by line.
# Default: "codes.txt"
CODES_FILE = "codes.txt"

# Role ID
# This is the ID of the role which is allowed to use the gen.
ROLE_ID = 867366769392091157

# imports here
import asyncio
import discord
from discord.ext import commands
import random
import aiofiles
import time
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)
gen_role = None
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all(), case_insensitive=True) # prefix here

async def getEmbed(type, arg=None): # change colours if you want to here 
    if type == 0:
        embed = discord.Embed(title="Sent you a code.", description="Check your DMs.", colour=discord.Colour.green())
        return embed
    elif type == 1:
        embed = discord.Embed(title="Here's your Generated Code.", description=arg, colour=discord.Colour.blue())
        return embed
    elif type == 2:
        embed = discord.Embed(title="Out of stock.", description="Generator is out of stock.", colour=discord.Colour.red())
        return embed
    elif type == 3:
        embed = discord.Embed(title="Timeout.", description=f"You are on timeout, retry in **{arg}**.", colour=discord.Colour.red())
        return embed
    elif type == 4:
        embed = discord.Embed(title="No Perms.", description=f"You do not have permission to execute this command.", colour=discord.Colour.red())
        return embed

async def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%dh %2dm %2ds" % (hour, minutes, seconds)

async def log(event, user=None, info=None): # logging in log.txt if you want to edit them
    now = datetime.now()
    timedata = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"
    
    writeable = ""
    
    if event == "generated":
        writeable += "[ GENERATE ] "
    elif event == "cooldown":
        writeable += "[ COOLDOWN ] "
    elif event == "no stock":
        writeable += "[ NO STOCK ] "
    elif event == "no dms":
        writeable += "[  NO DMS  ] "
    elif event == "bootup":
        writeable += "\n[  BOOTUP  ] "
    elif event == "ping":
        writeable += "[   PING   ] "
    elif event == "no perms":
        writeable += "[ NO PERMS ] "
    elif event == "userinfo":
        writeable += "[ USERINFO ] "
    elif event == "error":
        writeable += "[ CRITICAL ] "

    writeable += timedata
    
    try:
        writeable += f" ID: {user.id} User: {user.name}#{user.discriminator} // "
    except:
        writeable += f" // "
    
    if event == "generated":
        info = info.strip('\n')
        writeable += f"User was successfully sent code: {info}"
    elif event == "cooldown":
        writeable += f"User couldn't be sent a code as they are on a cooldown of {info}."
    elif event == "no stock":
        writeable += f"User couldn't be sent a code as there is no stock."
    elif event == "no dms":
        writeable += f"User couldn't be sent a code as their DMs were disabled."
    elif event == "bootup":
        writeable += "Bot was turned on."
    elif event == "ping":
        writeable += "User used the ping command."
    elif event == "no perms":
        writeable += f"User does not have the significant permissions for the {info} command."
    elif event == "userinfo":
        writeable += f"User used the userinfo command on: {info}"
    elif event == "error":
        writeable += info

    async with aiofiles.open(LOG_FILE, mode="a") as file:
        await file.write(f"\n{writeable}")
    
    if writeable.startswith("[ NO STOCK ]"):
        print(Fore.LIGHTYELLOW_EX + writeable.strip('\n'))
    elif writeable.startswith("[ CRITICAL ]"):
        for x in range(3):
            print(Fore.LIGHTRED_EX + writeable.strip('\n'))
    elif writeable.startswith("[  BOOTUP  ]"):
        print(Fore.LIGHTGREEN_EX + writeable.strip('\n'))

@bot.event
async def on_ready():
    global gen_role
    try:
        open(LOG_FILE, "x").close()
    except:
        pass
    try:
        open(CODES_FILE, "x").close()
    except:
        pass
    await log("bootup")
    for guild in bot.guilds:
        role = guild.get_role(ROLE_ID)
        if role != None:
            gen_role = role
            break
    if gen_role == None:
        await log("error", user=None, info=f"Cannot fetch role ({ROLE_ID}) from {bot.guilds[0].name}. Exiting in 5 seconds.")
        await asyncio.sleep(5)
        exit()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        time_retry = await convert(error.retry_after)
        await ctx.send(content = ctx.author.mention, embed = await getEmbed(3, time_retry))
        await log("cooldown", ctx.author, time_retry)
    elif isinstance(error, commands.MissingRole):
        await ctx.send(content = ctx.author.mention, embed = await getEmbed(4))
        await log("no perms", ctx.author, "generate")

@bot.command()
@commands.cooldown(1, 86400) # 1 is codes per cooldown // 86400 is the cooldown time (is in second)
@commands.has_role(ROLE_ID) # role for gen perms
@commands.guild_only()
async def generate(ctx):
    try:
        dm_msg = await ctx.author.send("Processing your request...")
    except:
        embed = discord.Embed(title="DMs are disabled!", description="Your dms are disabled. Enable them in Privacy Settings.", colour=discord.Colour.red())
        embed.set_image(url="https://cdn.discordapp.com/attachments/829087959331897364/850841491470548992/ezgif-2-ca6ebd5d9cfb.gif")
        await ctx.send(content=ctx.author.mention, embed=embed)
        await log("no dms", ctx.author)
        return
    async with aiofiles.open("codes.txt", mode="r") as file: # name of codes file
        file_lines = await file.readlines()
        try:
            code = random.choice(file_lines)
        except:
            await dm_msg.edit(embed=await getEmbed(type=2), content=ctx.author.mention)
            await ctx.send(embed=await getEmbed(type=2), content=ctx.author.mention)
            bot.get_command("generate").reset_cooldown(ctx)
            await log("no stock", ctx.author)
            return
        else:
            file_lines.remove(code)
    async with aiofiles.open("codes.txt", mode="w") as file: # name of codes file
        for line in file_lines:
            if file_lines[-1] != line:
                await file.write(line) 
            else: 
                await file.write(line.strip("\n"))
    await dm_msg.edit(embed=await getEmbed(type=1,arg=code), content=ctx.author.mention)
    await ctx.send(embed=await getEmbed(type=0), content=ctx.author.mention)
    await log("generated", ctx.author, code)

@bot.command()
async def userinfo(ctx, *, user : discord.Member = None):
    if user == None:
        user = ctx.author
    
    if gen_role in user.roles:
        des = f"Generator: `🟢`"
    else:
        des = f"Generator: `🔴`"
    
    embed = discord.Embed(color=discord.Colour.blue(), description=des, title=" ")
    embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=user.default_avatar_url)
    await ctx.send(embed=embed, content=ctx.author.mention)
    await log("userinfo", user=ctx.author, info=f"{user.name}#{user.discriminator}")

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Response Times", color=discord.Colour.blue()) # colour of ping command
    embed.add_field(name="API", value=f"`Loading...`")
    embed.add_field(name="Websocket", value=f"`{int(bot.latency * 1000)}ms`")
    time_before = time.time()
    edit = await ctx.send(embed=embed, content=f"{ctx.author.mention}")
    time_after = time.time()
    difference = int((time_after - time_before) * 1000)
    embed = discord.Embed(title="Response Times", color=discord.Colour.green()) # colour of ping command
    embed.add_field(name="API", value=f"`{difference}ms`")
    embed.add_field(name="Websocket", value=f"`{int(bot.latency * 1000)}ms`")
    await edit.edit(embed=embed, content=f"{ctx.author.mention}")
    await log("ping", ctx.author)

bot.run(TOKEN)