#!/usr/bin/python3
"""
7-base_geometry.py
"""


class BaseGeometry:
    """
    Base class representing geometry.

    This class serves as a base for other geometry-related classes.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
