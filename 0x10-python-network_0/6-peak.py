#!/usr/bin/python3
"""
   This module defines a function that finds a peak in a
   list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
       Finds a peak in a list of unsorted integers using a
       binary search-based approach.

       Args:
       - list_of_integers: A list of unsorted integers.

       Returns:
       - A peak element from the list.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
