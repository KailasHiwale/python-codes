#!/bin/python3

"""
Linear search
-------------
Time Complexity - O(n)
Use Case: Use if list is unsorted. 
"""


def lsearch(lst, item):
    """
    Takes in list and search item. Searches if item is present in the list
    returns index if present else returns -1
    
    :param list lst: list to be searched for item.
    :param int item: item for search.
    :return: item index or -1
    :rtype: int 

    """
    len_lst = len(lst)
    for i in range(len_lst):
        if lst[i] is item:
            return i
    return -1


if __name__ == '__main__':
    lst, item = [20, 10, 40, 23, 10, 50, 14], 23
    result = lsearch(lst, item)
    if result is not -1:
        print("Element at index {}".format(result))
    else:
        print("Not found")
