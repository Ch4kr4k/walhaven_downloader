import requests as re
import json
from creat import *


def main():

    base_url = 'https://wallhaven.cc/api/v1/'
    # category = 'Genshin+impact'
    category = input("search : ")
    # nsfw_url = '{}search?apikey=gmpvWw0NdWq3quPNm2NYJhXeK02MDmEj&q={}&categories=111&purity=111&atleast=1920x1080&sorting=random'.format(base_url,category)
    url = '{}search?q={}&categories=111&purity=110&sorting=random'.format(base_url, category)
    res = re.get(url)

    if res.status_code == 200:
        print("getting json value")
        json_data = json.loads(res.text)
        json_formated_data = json.dumps(json_data, indent=4)

        create_json(json_formated_data)

        finder_downloader()

    else:

        print("something went wrong")
        print(res.status_code)
        print(res.text)


if __name__ == '__main__':
    main()
