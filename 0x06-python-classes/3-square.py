#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """
    It is a square class with a private object attribute.
    It Checks the type of the argument and raises an exception on error
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """
    Return the current square area
    """

        def area(self):
            return self.__size ** 2
