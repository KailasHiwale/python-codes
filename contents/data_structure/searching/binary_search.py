#!/bin/python3
'''
:created on: Feb 16th 2019
:type: Interval/Binary search.
:time complexity: O(log n)
:constraint: Applicable for sorted arrays.
:summery: This algorithm search the provided element in the list by repeatedly dividing
    the list in two halfs.
:steps:
    1. check if low is less than or equal to high, if true got to 1.1 else 2.
        1.1 find mid positio: mid = low + (high - low) // 2
        1.2 if serach_element is at mid return mid.
        1.3 if serach_element is less than mid position element select the first half and 
            reapeat from step 1 again for first half.
        1.4 serach_element is greater than mid position element select the second half and 
            reapeat from step 1 again for first half.
    2. return -1
'''


def bsearch(lst, low, high, item):
    """Iterative binary search function"""
    while low <= high:                  # 1
        mid = low + (high - low) // 2   # 1.1
        if item is lst[mid]:            # 1.2
            return mid
        elif item < lst[mid]:           # 1.3
            high = mid - 1
        else:                           # 1.4
            low = mid + 1
    return -1                           # 2


# Start
if __name__ == '__main__':
    lst = [10, 20, 23, 30, 40, 50, 55]
    item, low, high = 50, 0, len(lst) - 1

    result = bsearch(lst, low, high, item)
    if result is not -1:
        print("Element at index {}".format(result))
    else:
        print("Not found.")
