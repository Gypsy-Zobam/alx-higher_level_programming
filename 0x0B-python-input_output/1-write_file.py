#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of c
    haracters written.
    """
    with open(filename, 'w', encoding="utf-8") as writefile:
        writefile.write(text)
        return len(text)
