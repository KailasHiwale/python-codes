#!/bin/python3
# Interpolation position formula:
# pos = low + [(item-lst[low])*(high-low) / (lst[high]-lst[low])]
# lst   -->     list
# item  -->     element to be search.
# low   -->     starting index in list.
# high  -->     End index in list


def interpolation_search(lst, low, high, item):
    """Iterative implementation of binary search function using
    interpotion formula.
    """
    while low <= high and item >= lst[low] and item <= lst[high]:
        # formula to find position
        pos = low + int(
            (item - lst[low]) * (high - low) / (lst[high] - lst[low]))

        if lst[pos] is item:
            return pos
        elif lst[pos] > item:
            high = pos - 1
        else:
            low = pos + 1
    return -1


# Start
if __name__ == '__main__':
    lst = [10, 20, 23, 30, 40, 50, 55]
    item, low, high = 50, 0, len(lst) - 1

    result = interpolation_search(lst, low, high, item)
    if result is not -1:
        print("Element at index {}".format(result))
    else:
        print("Not found.")
