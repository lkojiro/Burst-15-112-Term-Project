

import os


def getSongs():
    songs=[]
    this='/Users/logankojiro/desktop/pythonSketch/songs'
    for file in os.listdir(this):
        songs.append(file)
    return songs 



print(getSongs())