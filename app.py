import os
from flask import Flask

app = Flask(__name__)

@app.route("/slides/")
def slide_deck():
    return 'SLIDES!'

@app.route("/slide/<int:slide_id>")
def slide(slide_id):
    return 'SLIDE: %s' % (str(slide_id))

@app.route("/help")
def help():
    return "PUT DOCS HERE"

templates = {}
templates["index.html"] = '''
<!doctype html>
<html>
<head>
<title>{{ title }}</title>
</head>
<body>
{% block content %}
{% endblock %}
</body>
</html>
'''

templates["slides.html"] = '''
{% extends "index.html" %}

{% block content %}
# SONG HERE
{% endblock %}
'''

if __name__ == "__main__":
    app.run()
