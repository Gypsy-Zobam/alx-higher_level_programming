#!/usr/bin/python3
"""Function that returns the dictionary description with simple d
ata structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""

def class_to_json(obj):
    """Returns the dictionary description for JSON
    """
    return obj.__dict__
