#!/usr/bin/python3
"""
3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it's an instance of a cl
    ass that inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of, or if it's an instance
              of a class that inherited from,
              the specified class, otherwise False.
    """
    return (isinstance(obj, a_class))
