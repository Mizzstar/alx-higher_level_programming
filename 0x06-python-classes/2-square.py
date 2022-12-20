#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """repressent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
