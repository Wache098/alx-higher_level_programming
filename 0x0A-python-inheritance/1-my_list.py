#!/usr/bin/python3
'''1-my_list.py
'''


class MyList(list):
    """
    A subclass of the built-in list class that provides added functionality.
    """

    def print_sorted(self):
        """
        Print the list in sorted order (ascending).

        This method sorts the elements of the list in ascending order
        and prints the sorted list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
