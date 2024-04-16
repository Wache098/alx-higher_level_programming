#!/usr/bin/python3
"""
This module defines a Square class.
"""

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int or float, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparator for comparing two Square instances based on area.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of both squares is equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparator for comparing two Square instances based on area.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of both squares is not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparator for comparing two Square instances based on area.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is less than the area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparator for comparing two Square instances based on area.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is less than or equal to the area of the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparator for comparing two Square instances based on area.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is greater than the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparator for comparing two Square instances based on area.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is greater than or equal to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
