# Name: edited tag RTL Bug
# Description: Change the position of the "(edited)" tag
# Author: checksum (@0daySkid)
# Original founder: unknown

import requests
import sys

class Exploit:

    MAGIC_CHAR = '\u202b'

    def __init__(self, token, channel_id, message):
        self.token = token
        self.channel_id = channel_id
        self.message = message
        self.headers = {'Authorization': token}


    def execute(self):
        """ do the magik """
        message = f'{self.MAGIC_CHAR} {self.message} {self.MAGIC_CHAR}'

        res = requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': message})

        if res.status_code == 200:
            message_id = res.json()['id']

            requests.patch(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages/{message_id}', headers=self.headers, json={'content': ' ' + message})


def main():
    if len(sys.argv) < 4:
        print(f'Usage: py {sys.argv[0]} <token> <channel id> <message>')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]
    message = sys.argv[3]

    exploit = Exploit(token, channel_id, message)

    exploit.execute()


if __name__ == '__main__':
    main()
