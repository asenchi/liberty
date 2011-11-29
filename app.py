import os
import yaml
from flask import Flask, render_template, redirect, url_for

SONGS = "./songs"

app = Flask(__name__)
app.config.from_object(__name__)

def open_file(s):
    return yaml.load(file(s, 'r').read())

def build_song(d):
    if d["structure"]:
        d["final"] = []
        for s in d["structure"]:
            d["final"].append(d[s])
    d["final"] = "\n".join(d["final"])
    return d

def get_files(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            yield (filename, path)

def pretty_filename(f):
    return f.replace("_", " ").title().split('.')[0]

def toc(songs):
    sl = []
    for song in songs:
        filename = song[0].replace("_", "-").split('.')[0]
        sl.append((filename, pretty_filename(song[0])))
    return list(enumerate(sl, start=1))

@app.route("/")
def index():
    redirect(url_for('songs'))

@app.route("/songs/")
def songs():
    songlist = []
    for song in get_files(app.config["SONGS"]):
        songlist.append(song)
    songlist.sort()
    songs = toc(songlist)
    return render_template(
               "toc.html",
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
            compiled = build_song(opened)
    return render_template(
               "song.html",
               song=compiled["final"],
               title=compiled["title"]
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
