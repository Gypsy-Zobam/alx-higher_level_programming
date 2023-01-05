#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize square
        Args:
            size (int): size of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """Get value of the width
        Returns:
            width (int)
        """
    @width.setter
    def width(self, value):
        """Change the value of width
        Args:
            value (int): new value of width
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get value of the height
        Returns:
            height (int)
        """
    @height.setter
    def height(self, value):
        """change the value of the height
        Args:
        value (int): new value of the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
