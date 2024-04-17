#!/usr/bin/python3
"""
8-rectangle.py
"""


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.

    This class inherits from BaseGeometry and represents a rectangle with
    width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
