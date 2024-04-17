#!/usr/bin/python3
"""
101-add_attribute.py
"""


def add_attribute(obj, attribute, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attribute: The name of the attribute to add.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not isinstance(obj, object):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
