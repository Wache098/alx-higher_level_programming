#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The identity of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's position."""
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's position."""
        self.__y = value
