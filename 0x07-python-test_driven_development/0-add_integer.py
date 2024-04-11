#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers together and returns the result.

    Parameters:
        a (int or float): The first integer or float to be added.
        b (int or float, optional): The second integer or float to be added. Defaults to 98.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or float.

    Returns:
        int: The sum of 'a' and 'b', after casting them to integers if necessary.
        """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
