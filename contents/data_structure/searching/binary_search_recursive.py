#!/bin/python3

# Formula to find mid position
# mid = low + (high - low) // 2
# Time Complexity: O(log n)


def bsearch(lst, low, high, item):
    """Recursive binary search function"""
    if low <= high:
        mid = low + (high - low) // 2
        if lst[mid] is item:
            return mid
        elif lst[mid] > item:
            return bsearch(lst, low, mid - 1, item)
        else:
            return bsearch(lst, mid + 1, high, item)
    else:
        return -1


# Start
if __name__ == '__main__':
    lst = [10, 20, 23, 30, 40, 50, 55]
    item, low, high = 5, 0, len(lst) - 1

    result = bsearch(lst, low, high, item)
    if len(lst) > 0:
        if result is not -1:
            print("Element at index {}".format(result))
        else:
            print("Not found.")
    else:
        print("Can not search in empty list")
