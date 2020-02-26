#!/bin/python3


def sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot_value, left_half, right_half = lst[0], [], []
        for i in lst[1:]:
            if pivot_value > i:
                left_half.append(i)
            else:
                right_half.append(i)
        return sort(left_half) + [pivot_value] + sort(right_half)


if __name__ == "__main__":
    lst = list(map(
        int, input("Enter space seperated list\n").rstrip().split()))
    print("Sorted list is\n{}".format(sort(lst)))
