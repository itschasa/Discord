# Name: Delete Webhook
# Description: Forcefully delete a webhook
# Author: checksum (@0daySkid)
# Original founder: ~not an exploit l0l~

import requests
import sys

class Exploit:

    def __init__(self, url):
        self.webhook_url = url


    def execute(self):
        """ send DELETE request to webhook url """
        return requests.delete(self.webhook_url)

    
def main():
    if len(sys.argv) < 1:
        print(f'Usage: py {sys.argv[0]} <webhook url>')
        sys.exit()

    webhook_url = sys.argv[1]

    exploit = Exploit(webhook_url)

    exploit.execute()


if __name__ == '__main__':
    main()
