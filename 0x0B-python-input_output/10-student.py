#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attr
        ibutes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """

        if attrs is not None:
            res ={k: self.__dict__[k] for k in self.__dict__.keys() &attr}
            return res
        else:
            return self.__dict__


