import os
import yaml

def table_contents():
    pass

def inkey(key):
    pass

def speed(spd):
    pass

def license(song):
    pass

def song(song):
    pass

def open_file(path):
    return file(path, 'r').read()

def yamlize(string):
    return yaml.load(string)

def build_song(serial, raw):
    if raw:
        serial["raw"] = raw
    if serial["structure"]:
        serial["final"] = []
        # Loop through our structure and build a Python structure of our song
        for idx, struct in enumerate(serial["structure"]):
            if type(struct) is list:
                slide = []
                for part in struct:
                    slide.append(serial[part].split('\n'))
                serial["final"].append(slide)
    return serial

def get_files(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
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

def in_key(songs, key):
    sl = []
    for filename, path in songs:
        opened = open_file(path)
        serialized = yamlize(opened)
        if not serialized.get("inkey"):
            continue
        if serialized["inkey"] == str(key):
            href = filename.replace("_", "-").split('.')[0]
            sl.append((href, pretty_filename(filename)))
    return list(enumerate(sl, start=1))

def in_speed(songs, speed):
    sl = []
    for filename, path in songs:
        opened = open_file(path)
        serialized = yamlize(opened)
        if not serialized.get("speed"):
            continue
        if serialized["speed"] == str(speed):
            href = filename.replace("_", "-").split('.')[0]
            sl.append((href, pretty_filename(filename)))
    return list(enumerate(sl, start=1))
