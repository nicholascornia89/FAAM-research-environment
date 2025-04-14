import json, csv
from time import gmtime, strftime
import os


def json2dict(json_filename):  # imports a JSON file as dictionary
    with open(json_filename, "r") as f:
        json_file = json.load(f)
        return json_file


def dict2json(d, json_filename):  # export a dictionary to JSON file
    json_file = open(json_filename, "w")
    json.dump(d, json_file, indent=2, ensure_ascii=False)


def get_current_date():
    return strftime("%Y-%m-%d", gmtime())


def get_latest_file(basepath):  # returns latest file path in a directory
    files = os.listdir(basepath)
    paths = [os.path.join(basepath, basename) for basename in files]
    return max(paths, key=os.path.getctime)
