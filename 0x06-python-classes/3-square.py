#!/usr/bin/python3
"""class Square"""


class Square:
    """Private instance attribute and instantation with optional"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

            def area(self):
                """area of square"""
                return self.__size ** 2
