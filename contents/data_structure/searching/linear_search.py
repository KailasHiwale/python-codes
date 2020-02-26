#!/bin/python3


def lsearch(lst, item, len_lst):
    """Linear search"""
    for i in range(len_lst):
        if lst[i] is item:
            return i
    return -1


if __name__ == '__main__':
    lst, item = [20, 10, 40, 23, 10, 50, 14], 23
    len_lst = len(lst)
    result = lsearch(lst, item, len_lst)
    if result is not -1:
        print("Element at index {}".format(result))
    else:
        print("Not found")
