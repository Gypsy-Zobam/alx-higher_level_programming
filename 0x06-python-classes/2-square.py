#!/usr/bin/python3
'''Define a class Square'''

class Square:
    ''' It is a square class with a private instance attribute.
    Raise TypeError and ValueError exceptions'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
