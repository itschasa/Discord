# Config

# Length of Captcha
length = 6

# Bot Token
TOKEN = ""

import discord
from discord.ext import commands
import random
from captcha.image import ImageCaptcha
import string
import json
import os

bot = commands.Bot(command_prefix="=", case_insensitive=True, intents=discord.Intents.all())

config = None
verify_channel = None
verify_role = None
verify_guild = None

@bot.event
async def on_ready():
    global config
    global verify_channel
    global verify_role
    global verify_guild
    print(f"{bot.user} is online.")
    print("Loading Config..")
    try:
        config = json.loads(open("config.json", "r").read())
    except:
        print("No config found! Run =setup in your server!")
    else:
        verify_guild = bot.get_guild(config["guild"])
        verify_channel = bot.get_channel(config["channel"])
        verify_role = verify_guild.get_role(config["role"])
        print("Loaded Config!")
        

@bot.event
async def on_member_join(member):
    global config
    global verify_channel
    global verify_role
    global verify_guild
    if member.guild.id == int(config["guild"]):
        await member.add_roles(verify_role)
        text = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(length))
        file_name = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(20))
        image = ImageCaptcha(width=280, height=90)
        captcha = image.generate(text)
        image.write(text, f"captchas\\{file_name}.png")
        file = discord.File(f"captchas//{file_name}.png", filename=f"{file_name}.png")
        embed = discord.Embed(title="Verification", description="This server is using Captcha Verification\n to protect their server.\n\nPlease type out the letters you see in\nthe captcha below.\n\n**Note:** The captcha is **case-sensitive.**\n\nYou have **30 seconds** to reply.", color=0x9f4fd1, image=f"attachment://")
        embed.set_image(url=f"attachment://{file_name}.png")
        del_msgs = []
        msg = await verify_channel.send(content=member.mention, embed=embed, file=file)
        del_msgs.append(msg)
        def wait_for_reply(message):
            return message.channel == verify_channel and message.author == member
        for x in range(3):
            try:
                rpy = await bot.wait_for("message", check=wait_for_reply, timeout=30)
            except:
                try: await member.kick(reason="Verification Timeout.")
                except: pass
                break
            else:
                if rpy.content == text:
                    await member.remove_roles(verify_role)
                    for x in del_msgs:
                        await x.delete()
                    await rpy.delete()
                    return
                else:
                    if x != 2:
                        msg = await verify_channel.send(f"{member.mention} Invalid, you have {2 - x} attempts left.")
                        del_msgs.append(msg)
                        del_msgs.append(rpy)
        try: await member.kick(reason="Too many attempts.")
        except: pass
        for x in del_msgs:
            try:
                await x.delete()
            except:
                continue
        await rpy.delete()

@bot.event
async def on_channel_create(channel):
    global config
    global verify_channel
    global verify_role
    global verify_guild
    if channel.id == int(config["channel"]):
        try:
            overwrites = {verify_role: discord.PermissionOverwrite(
                read_messages=False,
                send_messages=False,
                add_reactions=False
            )}
            await channel.edit(overwrites=overwrites)
        except:
            pass

@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    if os.path.exists("config.json"):
        await ctx.send("config.json already exists!")
        return
    global config
    msg = await ctx.send("Setting up guild...")
    role = await ctx.guild.create_role(name="Verifing")
    for channel in ctx.guild.channels:
        try:
            overwrites = {role: discord.PermissionOverwrite(
                read_messages=False,
                send_messages=False,
                add_reactions=False
            )}
            await channel.edit(overwrites=overwrites)
        except:
            pass
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(
            read_messages=False,
            send_messages=False,
        ),
        role: discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True,
        )
    }
    channel = await ctx.guild.create_text_channel(name="verify-here", overwrites=overwrites, slowmode_delay=10)
    con_json = {"role": role.id, "channel": channel.id, "guild": ctx.guild.id}
    config = con_json
    conf = open("config.json", "a")
    conf.write(json.dumps(con_json))
    conf.close()
    await msg.edit(content="Finished Setup!")

@bot.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def perms_setup(ctx):
    if not os.path.exists("config.json"):
        await ctx.send("config.json doesn't exists!")
        return
    global config
    msg = await ctx.send("Rechecking perms...")
    for channel in ctx.guild.channels:
        try:
            overwrites = {verify_role: discord.PermissionOverwrite(
                read_messages=False,
                send_messages=False,
                add_reactions=False
            )}
            await channel.edit(overwrites=overwrites)
        except:
            pass
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(
            read_messages=False,
            send_messages=False,
        ),
        verify_role: discord.PermissionOverwrite(
            read_messages=True,
            send_messages=True,
        )
    }
    await msg.edit("Finished Setup!")

bot.run(TOKEN)
