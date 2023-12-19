#name: Muyiwa J. Obadara
#date: December 19, 2023
"""
A Search Module which inplements various searching algorithms
such as Linear Search and binary Search
"""

from typing import Union

def linear_search(arr, el):
    """
    Search Algorithm: Linear Search

    Returns the index in arr where el
    is found. If el is not found in arr,
    None is returned.
    @args: arr: list or tuple
    @return: index where the element was found.
    Example
    ==============
    >>> linear_search([1, 2, 3, 4], 3)
    2

    >>> linear_search([1, 2, 3, 4], 5)
    None
    """
    found = False
    for i in range(len(arr)):
        if arr[i] == el:
            found = True
            return i
    
    if not found:
        return None
    
def binary_search(arr, el):
    """
    Search Algorithm: Binary Search
    
    Returns the index in arr where el
    is found. If el is not found in arr,
    None is returned.
    @args: arr: list or tuple
    @return: index where the element was found.
    Example
    ==============
    >>> binary_search([1, 2, 3, 4], 3)
    2

    
    >>> binary_search([1, 2, 3], 5)
    None
    """
    found = False
    if len(arr) == 1: found = True
    else:
        middle_index = int(len(arr) / 2) + 1
        if el == arr[middle_index]:
            found = True
        elif el < arr[middle_index]:
            arr = arr[:middle_index]
            binary_search(arr, el)
        else:
            arr = arr[middle_index:]
            binary_search(arr, el)
    return found

print(binary_search([1, 2, 3, 4, 5, 6, 7], 2))
