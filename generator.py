import os
import yaml

def verify_filename(str, set):
    return False in [c in str for c in set]

def open_file(path):
    if not verify_filename(path, '-'):
        print("Filename's should contain only letters, numbers and underscores.")
        raise
    try:
        f = open(path, 'r')
        contents = f.read()
    finally:
        f.close()
    return contents

def yamlize(string):
    try:
        return yaml.safe_load(string)
    except Exception:
        print(string)
        print("Only one song should be defined per file. Songs are defined by the '---' at the top. See documentation")
        raise

def build_song(serial, raw):
    if raw:
        serial["raw"] = raw
    if serial["structure"]:
        serial["final"] = []
        # Loop through our structure and build a Python structure of our song
        for idx, struct in enumerate(serial["structure"]):
            if type(struct) is list:
                slides = []
                for part in struct:
                    slides.append(serial[part].split('\n'))
                serial["final"].append(slides)
    return serial

def get_files(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and not filename.startswith('.'):
            yield (filename, path)

def pretty_filename(f):
    return f.replace("_", " ").title().split('.')[0]

def toc(songs):
    songs.sort()
    sl = []
    for filename, path in songs:
        href = filename.replace("_", "-").split('.')[0]
        sl.append((href, pretty_filename(filename)))
    return list(enumerate(sl, start=1))

def in_attr(attr, songs, val):
    sl = []
    for filename, path in songs:
        opened = open_file(path)
        serialized = yamlize(opened)
        if not serialized.get(attr):
            continue
        if serialized[attr] == str(val):
            href = filename.replace("_", "-").split('.')[0]
            sl.append((href, pretty_filename(filename)))
    return list(enumerate(sl, start=1))
