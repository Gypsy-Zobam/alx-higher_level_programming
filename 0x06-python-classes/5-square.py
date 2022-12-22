#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialize square
        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """Gets value of size
        Returns:
            size (int)
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Change the value of size
        Args:
            value (int): new value of size
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of a square area
        Returns:
            area
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints the stdout of the square with the character #.
        """

        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
