#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square
        Args:
            size (int): size of the square
            position (int, int): position of argument
        """

        self.size = size
        self.position = position

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
        """ Calculates the area of a square
        Returns:
            area
        """

        return self.__size ** 2

    @property
    def position(self):
        """Gets the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """change the value of position
        Args:
            value (int, int): new position
        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        a = self.__size ** 2
        return a

    def my_print(self):
        """
        Prints the stdout of the square with the character #.
        """

        if self.__size == 0:
            print("")
        else:
            for line in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for space in range(0, self.__position[0]):
                print(" ", end="")
                for j in range(0, self.__size):
                print("#", end="")
            print()
