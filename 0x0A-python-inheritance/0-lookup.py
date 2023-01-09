#!/usr/bin/python3
"""Return the list of avaliable attributes and methods of an object
"""


def lookup(obj):
    """Returns a list object
    Args:
        obj(_type_): an object to be used
    Returns:
        dir(obj)
    """
    return dir(obj)
