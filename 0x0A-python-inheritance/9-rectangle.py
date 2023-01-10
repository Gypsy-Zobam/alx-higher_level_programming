#!/usr/bin/python3
"""9. Full rectangle. Rectangle inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that calculates area of rectangle
        """

        return self.width * self.height

    def __str__(self):
        """Returns a formatted string."""

        return str(f"[Rectangle] {self.__width}/{self.__height}")
