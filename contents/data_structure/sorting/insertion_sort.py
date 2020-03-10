#!/bin/python3

"""
# Time complexity:
    1. Best case: O(n)
    2. Average case: O(n2)
    3. Worst case: O(n2)
# Space complexity: O(1)
# Stable, Inplace and 
# better than selection sort and buble sort in practical cases
"""


def sort(lst, lst_length):
    for i in range(1, lst_length):
        value, hole = lst[i], i
        while hole > 0 and lst[hole - 1] > value:
            lst[hole] = lst[hole - 1]
            hole -= 1
        lst[hole] = value
    return lst


if __name__ == '__main__':
    lst_length = int(input("Enter lenght of list\n"))
    lst = list(map(
        int, input("Enter space seperated list\n").rstrip().split()))
    print("Sorted list is\n{}".format(sort(lst, lst_length)))
