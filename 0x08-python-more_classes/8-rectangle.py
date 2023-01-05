#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """The Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """Instance methods that return the area
        and perimeter of a rectangle"""
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """Print the rectangle with the character #"""
    def __str__(self):
        rect = ""

        if self.width == 0 or self.height == 0:
            return rect
        for i in range(self.height):
            for j in range(self.width):
                rect += str(self.print_symbol)

            if i != self.height - 1:
                rect += '\n'
        return rect

    """Return a string representation of the instance creation"""
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    """Delete when an instance delete is run"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """Returns the biggest rectangle based on the area"""
    @static method
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() <rect_2.area():
            return rect_2
        else:
            return rect_1
