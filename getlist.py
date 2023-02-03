import os


dir_path = '/home/chakrak/ws/proj/py/pics/down'
nsfw = '/home/chakrak/ws/proj/py/pics/nsfw'


def getlist():
    list_of_wall = []
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            list_of_wall.append(path)
    return list_of_wall


def getlist_nsfw():
    list_of_nsfw = []
    for path in os.listdir(nsfw):
        # check if current path is a file
        if os.path.isfile(os.path.join(nsfw, path)):
            list_of_nsfw.append(path)
    return list_of_nsfw
