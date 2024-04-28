#!/usr/bin/python3
"""Defines the Base class."""



class Base:
    """Represents the base class for other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance.

        Args:
            id (int): The id of the Base instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
