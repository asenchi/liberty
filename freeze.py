from flask_frozen import Freezer

from generator import *
from app import app

freezer = Freezer(app)

@freezer.register_generator
def song():
    songlist = get_files(app.config["SONGS"])
    for song, path in songlist:
        title = song.split('.')[0].replace("_", "-")
        yield { 'title': title }

if __name__ == '__main__':
    freezer.freeze()
