import requests
import os
import sys
from getlist import *
import time


def search(name):
    url = f"https://wallhaven.cc/api/v1/search?q={name}&categories=111&purity=110&sorting=random"
    res = requests.get(url)
    json_data = res.json()
    dlinks = []

    for wall in json_data["data"]:
        dlinks.append(wall["path"])

    return dlinks


def main():
    wal = '/home/chakrak/ws/proj/py/pics/down'
    nsfw = '/home/chakrak/ws/proj/py/pics/nsfw'
    name = input("name: ")
    dir_v = ""
    while not (dir_v == 1 or dir_v == 2):
        dir_v = int(input("choose directory\n1 for down\n2 for nsfw : "))

    if dir_v == 1:
        d_dir = wal
    elif dir_v == 2:
        d_dir = nsfw

    while True:
        walurl = search(name)
        # print(f"link :: name")
        # count = 0
        downloaded = getlist()
        downloadedns = getlist_nsfw()
        for i in walurl:
            # count=count+1
            wname = i[31:]
            if (wname in downloaded) or (wname in downloadedns):

                print(f"downloaded= {i} :: {i[31:]}")
            else:
                print(f"not downloaded= {i} :: {i[31:]}\n Downloading....")
                os.system('wget {} -P {}'.format(i, d_dir))
        time.sleep(3)
    # print(f"total photos = {count}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
