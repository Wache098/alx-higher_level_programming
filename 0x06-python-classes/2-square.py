#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:

    """
    This class represents a Square.
    """


def __init__(self, size=0):
    """
    Initializes a new Square instance.

    Args:
    size(int, optional): the size of a square .Defaults to 0.

    Raises:
    TypeError: If size is no integer.
    ValueError:If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
