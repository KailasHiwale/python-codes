#!/bin/python3


def merge(left, right, lst):
    len_left, len_right, i, j, k = len(left), len(right), 0, 0, 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        lst[k] = right[j]
        j += 1
        k += 1

    return lst


def sort(lst):
    n = len(lst)
    if n < 2: return lst
    MID = n // 2
    left_half = sort(lst[:MID])
    right_half = sort(lst[MID:])
    return merge(left_half, right_half, lst)


if __name__ == "__main__":
    lst = list(map(
        int, input("Enter space seperated list\n").rstrip().split()))
    print("Sorted list\n{}".format(sort(lst)))

