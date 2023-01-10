#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”
"""

import json

def load_from_json_file(filename):
    """Create an object from a json file"""

    with open(filename, "r", encoding="utf-8") as readFile:
        return json.load(readFile)
