#!/usr/bin/python3
"""Class that defines a student
"""

class Student:
    """Public instance attributes of student data
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """It retrieves a dictionary representation.
        """
        return self.__dict__
