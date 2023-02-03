import requests
from getlist import *


def search(name):
    url = f"https://wallhaven.cc/api/v1/search?q={name}&categories=111&purity=110&sorting=random"
    res = requests.get(url)
    json_data = res.json()
    dlinks = []

    for wall in json_data["data"]:
        dlinks.append(wall["path"])

    return dlinks


def main():
    name = input("name: ")
    walurl = search(name)
    print(f"link :: name")
    count = 0
    downloaded = getlist()
    downloadedns = getlist_nsfw()
    for i in walurl:
        count = count+1
        wname = i[31:]
        if (wname in downloaded) or (wname in downloadedns):
            print(f"downloaded= {i} :: {i[31:]}")
        else:
            print(f"not downloaded= {i} :: {i[31:]}")
    print(f"total photos = {count}")


if __name__ == '__main__':
    main()
