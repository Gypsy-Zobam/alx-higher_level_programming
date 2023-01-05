#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """Defining a Rectangle class"""

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
        return self.__width

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
        return self.__height

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

    """Instance methods that return the area and perimeter of a rectangle"""

    def area(self):
        """Calculates the area of a rectangle
        Returns:
            area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Perimeter of the rectangle.
        """

        if self.width == 0 or self.height == 0
            return 0
        return 2 * (self.width + self.height)
