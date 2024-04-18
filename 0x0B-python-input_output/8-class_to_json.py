#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary description of the object for JSON serialization.
    """
    # print("type of obj --> {}".format(type(obj)))
    return obj.__dict__
