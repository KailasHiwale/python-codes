#!/bin/python3

# Formula to find mid position
# mid = low + (high - low) // 2
# Time Complexity: O(log n)


def bsearch(lst, low, high, item):
    """Iterative binary search function"""
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] is item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Start
if __name__ == '__main__':
    lst = [10, 20, 23, 30, 40, 50, 55]
    item, low, high = 50, 0, len(lst) - 1

    result = bsearch(lst, low, high, item)
    if result is not -1:
        print("Element at index {}".format(result))
    else:
        print("Not found.")
