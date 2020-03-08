#!/bin/python3
# Interpolation position formula:
# pos = low + [(item-lst[low])*(high-low) / (lst[high]-lst[low])]
# lst   -->     list
# item  -->     element to be search.
# low   -->     starting index in list.
# high  -->     End index in list
# Time complexity: O(log log n)
# Time complexity worst case: O(n)
# Auxilary space: O(1)


def interpolation_search(lst, low, high, item):
    """Recursive implementation of binary search function using
    interpotion formula.
    """
    if low <= high and item >= lst[low] and item <= lst[high]:
        # formula to find position
        pos = low + int(
            (item - lst[low]) * (high - low) // (lst[high] - lst[low]))

        if lst[pos] is item:
            return pos
        elif lst[pos] > item:
            return interpolation_search(lst, low, pos - 1, item)
        else:
            return interpolation_search(lst, pos + 1, high, item)
    else:
        return -1


# Start
if __name__ == '__main__':
    lst = [10, 20, 23, 30, 40, 50, 55]
    item, low, high = 5, 0, len(lst) - 1

    result = interpolation_search(lst, low, high, item)
    if result is not -1:
        print("Element at index {}".format(result))
    else:
        print("Not found.")
