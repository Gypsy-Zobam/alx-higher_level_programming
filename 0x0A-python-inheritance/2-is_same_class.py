#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an intance of the specified class; otherwise False.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
