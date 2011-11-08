import os
import yaml
from flask import Flask

SONGS = "./songs"

app = Flask(__name__)
app.config.from_object(__name__)

def open_song(s):
    return yaml.load(file(s, 'r').read())

def struct(d):
    if d["structure"]:
        d["final"] = []
        for s in d["structure"]:
            d["final"].append(d[s])
    d["final"] = "\n".join(d["final"])
    return d

def get_songs(d):
    for song in os.listdir(d):
        path = os.path.join(d, song)
        if os.path.isfile(path):
            yield (song, path)

def cleanse_file(f):
    return f.replace("_", " ").title().split('.')[0]

def toc(songs):
    sl = []
    sl.append("<pre>\n")
    for song in songs:
        sl.append("* %s" % cleanse_file(song[0]))
    sl.append("</pre>\n")
    return "\n".join(sl)

@app.route("/songs/")
def songs():
    songlist = []
    for song in get_songs(app.config["SONGS"]):
        songlist.append(song)
    songlist.sort()
    songs = toc(songlist)
    return songs

@app.route("/song/<title>")
def song(title):
    render = []
    cleanse = title.replace("-", "_")
    songlist = get_songs(app.config["SONGS"])
    for song, path in songlist:
        if song.split('.')[0] == cleanse:
            opened = open_song(path)
            compiled = struct(opened)
            render.append("<pre>\n")
            render.append(compiled["final"])
            render.append("</pre>\n")
    return "\n".join(render)

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
    app.run(host="0.0.0.0",port=8080)
