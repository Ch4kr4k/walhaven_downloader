import os
from getlist import getlist
from getlist import getlist_nsfw

wal = '/home/chakrak/ws/proj/py/pics/down'
nsfw = '/home/chakrak/ws/proj/py/pics/nsfw'


def create_json(json_formated_data):

    with open('json.txt', 'w') as f:
        for x in json_formated_data:
            f.write(x)


def finder_downloader():
    d_dir = None
    downloaded = []
    downloaded_nsfw = []
    downloaded = getlist()
    downloaded_nsfw = getlist_nsfw()
    dir_v = 0
    while not (dir_v == 1 or dir_v == 2):
        dir_v = int(input("choose directory\n1 for down\n2 for nsfw : "))

    if dir_v == 1:
        d_dir = wal
    elif dir_v == 2:
        d_dir = nsfw
    else:
        print("directory not found")
        exit(0)

    print(f'{d_dir} directory selected')

    with open('json.txt', 'r') as f:

        lines = f.readlines()

        for line in lines:

            if 'path' in line:
                link = line[21:-3]
                filename = line[52:-3]
                if filename in downloaded or filename in downloaded_nsfw:
                    print("already downloaded skipping")
                    continue

                else:
                    print("Donwloading")
                    os.system('wget {} -P {}'.format(link, d_dir))
