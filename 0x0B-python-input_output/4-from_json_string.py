#!/usr/bin/python3
""" 4-from_json_string.py"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python data struct

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
