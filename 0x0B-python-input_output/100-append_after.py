#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each
    line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each
        line containing the search string.
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
