#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    """
    Class representing a rebel integer.

    This class inherits from int and has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Override the equality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return (super().__eq__(other))
