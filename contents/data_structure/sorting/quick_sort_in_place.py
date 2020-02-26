#!/bin/python3


def partition(lst, start_indx, end_indx):
    pivot_value = lst[end_indx]
    pivot_indx = start_indx
    for i in range(start_indx, end_indx):
        if lst[i] <= pivot_value:
            lst[i], lst[pivot_indx] = lst[pivot_indx], lst[i]
            pivot_indx += 1
    lst[pivot_indx], lst[end_indx] = lst[end_indx], lst[pivot_indx]
    return pivot_indx


def sort(lst, start_indx, end_indx):
    if len(lst) <= 1:
        return lst

    if start_indx < end_indx:
        pivot_indx = partition(lst, start_indx, end_indx)
        sort(lst, start_indx, pivot_indx - 1)
        sort(lst, pivot_indx + 1, end_indx)
    return lst


if __name__ == "__main__":
    lst = list(map(
        int, input("Enter space seperated list\n").rstrip().split()))
    start_indx, end_indx = 0, len(lst) - 1
    print("Sorted list is\n{}".format(sort(lst, start_indx, end_indx)))
