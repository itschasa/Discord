import threading
import requests
import ctypes
from easygui import fileopenbox

timeout = 10
checked = 0
working = 0

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def verify_list(proxy_list):
    global timeout, checked, working
    working_list = []
    for prox in proxy_list:
        try:

            proxy_dict = {
                "http": "http://"+prox+"/",
            }

            r = requests.get("http://ipinfo.io/json", proxies=proxy_dict, timeout=timeout)
            site_code = r.json()
            working_list.append(prox)
            f = open('good_proxies_list.txt', 'a')
            f.write(f"{prox}\n")
            f.close()
            working += 1
        except Exception as e:
            pass
        checked += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Hits: {working} - Checked: {checked}/{global_proxy}")

proxies = open(fileopenbox(title="Load HTTP Proxies", default="*.txt"), 'r', encoding="utf8", errors='ignore').read().split('\n')
proxies = list(dict.fromkeys(proxies))
global_proxy = len(proxies)
split = split_list(proxies, int(input(f"Threads? (no more than {global_proxy}): ")))
for x in split:
    threading.Thread(target=verify_list, args=(x,)).start()