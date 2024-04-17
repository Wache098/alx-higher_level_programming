#!/usr/bin/python3
"""
11-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.

    This class inherits from Rectangle and represents a square with equal
    sides (width and height).
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
