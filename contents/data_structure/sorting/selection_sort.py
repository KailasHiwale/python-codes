#!/bin/python3/

"""
:time complexity: O(n2)
:space complexity: O(1)
:stability: Stable, Inplace and Slow sorting algorithm.
:summery: 
    1. select the min.
    2. find the value less than min index value in remaining part
    3. if found replace min index value with the found min value
    4. increase the min index by one and repeat all the steps n-1 times
"""


# Function to implement selection sort algorithm.
def selection_sort(lst, n):
    lst, swap_count = list(lst), 0
    for i in range(n - 1):
        MIN = i
        for j in range(i + 1, n):
            if lst[MIN] > lst[j]:
                MIN = j
        if lst[MIN] != lst[i]:
            swap_count += 1
            lst[MIN], lst[i] = lst[i], lst[MIN]
    return lst, swap_count


if __name__ == "__main__":
    n = int(input("Enter length of list\n"))
    lst = map(int, input("Enter space seperated list\n").rstrip().split())
    sorted_list, swap_count = selection_sort(lst, n)
    print("Sorted list is {}".format(sorted_list))
    print("List is sorted in {} swaps".format(swap_count))
