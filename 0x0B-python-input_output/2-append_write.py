#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """Appends a str at end of a txt file and returns the no of characters add

    Args:
        filename (str): The name of the file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        num_characters_added = file.write(text)
    return num_characters_added
