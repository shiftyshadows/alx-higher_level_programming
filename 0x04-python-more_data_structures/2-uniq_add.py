#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    # Iterate over each element in the list
    for element in my_list:
        # Check if the element is an integer
        if isinstance(element, int):
            # Add the integer to the set
            unique_set.add(element)

    # Calculate the sum of unique integers
    total_sum = sum(unique_set)

    return total_sum
