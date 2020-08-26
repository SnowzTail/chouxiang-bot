import os
import eyed3
import json
import io
import collections


def info():
    path = 'assets/'
    artist_list = []
    for file_name in os.listdir(path):
        song = eyed3.load(os.path.join(path, file_name))
        artist_list.append(song.tag.artist)
    dict = {}
    for key in artist_list:
        dict[key] = dict.get(key, 0) + 1
    return collections.OrderedDict(sorted(dict.items()))


def save(dict):
    with open('artist.json', 'w', encoding='utf-8') as fp:
        json.dump(dict, fp)


if __name__ == '__main__':
    save(info())
