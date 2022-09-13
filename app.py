#!/usr/bin/env python

import os
import json

import yaml
from flask import Flask, render_template, redirect, url_for, send_from_directory

from generator import *

SONGS = "./songs"
FREEZER_DEFAULT_MIMETYPE = "text/html"
FREEZER_IGNORE_MIMETYPE_WARNINGS = True

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

@app.route("/song/<title>/")
def song(title):
    # We use '_' for filenames, match this with what we find.
    cleanse = title.replace("-", "_")
    songlist = get_files(app.config["SONGS"])
    for song, path in songlist:
        if song.split('.')[0] == cleanse:
            opened     = open_file(path)
            serialized = yamlize(opened)
            compiled   = build_song(serialized)
    total=len(compiled["final"])
    return render_template(
               "song.html",
               song=compiled["final"],
               title=compiled["title"],
               total=total,
           )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

@app.route("/help/")
def help():
    docs = open('DOCS.txt', 'r').read()
    return render_template(
            "help.html",
            docs=docs,
            title = "How to structure a song"
           )

@app.route("/creed/")
def creed():
    return render_template(
            "creed.html",
            title = "Apostle's Creed"
           )

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
