import os
from getlist import getlist
import random


def set_wallpaper():
    dest = '/home/chakrak/.config/background'
    list = []
    list = getlist()
    wal = random.choice(list)
    os.system(
        'cp /home/chakrak/ws/proj/py/pics/down/{} /home/chakrak/ws/proj/py/wal'.format(wal))
    os.system('mv /home/chakrak/ws/proj/py/wal/{} {}'.format(wal, dest))
