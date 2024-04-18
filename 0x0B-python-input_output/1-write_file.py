#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """Writes a string to txt file and returns the no of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters
