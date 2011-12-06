import os
import json

import yaml
from flask import Flask, render_template, redirect, url_for

from generator import *

SONGS = "./songs"

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/songs.json")
def raw():
    songlist = get_files(app.config["SONGS"])
    songs = []
    for song, path in songlist:
        opened     = open_file(path)
        serialized = yamlize(opened)
        compiled   = build_song(serialized, opened)
        songs.append(compiled)
    return json.dumps(songs, sort_keys=True, indent=4)

@app.route("/")
def index():
    return redirect(url_for('songs'))

@app.route("/songs/")
def songs():
    songs = {}
    songlist = list(get_files(app.config["SONGS"]))
    songlist.sort()
    songs["song_list"] = toc(songlist)
    return render_template(
               "song_list.html",
               songs=songs,
               title="Table of Contents"
           )

@app.route("/song/<title>")
def song(title):
    # We use '_' for filenames, match this with what we find.
    cleanse = title.replace("-", "_")
    songlist = get_files(app.config["SONGS"])
    for song, path in songlist:
        if song.split('.')[0] == cleanse:
            opened = open_file(path)
            serialized = yamlize(opened)
            compiled = build_song(serialized, raw)
    return render_template(
               "song.html",
               song=compiled["final"],
               title=compiled["title"],
               raw=compiled["raw"]
           )

@app.route("/songs/inkey/<key>")
def inkey(key):
    songlist = list(get_files(app.config["SONGS"]))
    songs = {}
    songs[key] = in_key(songlist, key)
    songs[key].sort()
    title = "Songs in the key of %s" % key.capitalize()
    return render_template(
               "song_list.html",
               songs=songs,
               title=title
           )

@app.route("/songs/bykey/")
def bykey():
    songlist = list(get_files(app.config["SONGS"]))
    songs = {}
    for letter in ["a", "b", "c", "d", "e", "f", "g"]:
        songs[letter] = in_key(songlist, letter)
        songs[letter].sort()
    return render_template(
               "song_list.html",
               songs=songs,
               title = "Songs sorted by key"
           )

@app.route("/songs/byspeed/")
def byspeed():
    songlist = list(get_files(app.config["SONGS"]))
    songs = {}
    for spd in ["slow", "fast"]:
        songs[spd] = in_speed(songlist, spd)
        songs[spd].sort()
    return render_template(
               "song_list.html",
               songs=songs,
               title = "Songs sorted by speed"
           )

@app.route("/help")
def help():
    return "PUT DOCS HERE"

# templates = {}
# templates["index.html"] = '''
# <!doctype html>
# <html>
# <head>
# <title>{{ title }}</title>
# </head>
# <body>
# {% block content %}
# {% endblock %}
# </body>
# </html>
# '''
#
# templates["slides.html"] = '''
# {% extends "index.html" %}
#
# {% block content %}
# # SONG HERE
# {% endblock %}
# '''

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
