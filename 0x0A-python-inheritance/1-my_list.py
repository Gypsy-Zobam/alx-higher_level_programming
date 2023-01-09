#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class that inherits from list
    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """prints the sorted list"""
        new_list = self[:]
        new_list.sort()
        print(f"{} (new_list)")

