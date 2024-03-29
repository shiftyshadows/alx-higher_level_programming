#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate over each element in the original list
    for element in my_list:
        # Check if the element matches the search element
        if element == search:
            # If it matches, append the replace element to the new list
            new_list.append(replace)
        else:
            # If it doesn't match, append the original element to the new list
            new_list.append(element)

    return new_list
