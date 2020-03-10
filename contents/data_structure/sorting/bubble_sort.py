#!/bin/python3
"""
# Time Complexity:
    1. Best case: O(n)
    2. Average case: O(n2)
    3. Worst case: O(n2)
# Space complexity: O(1)
# Stable & In place sorting algorithm.
# Slow sorting algorithm but better than selection sort.

"""


# bubble_sort function to find number of swap, first element & last element.
def bubble_sort(a, n):
    swap_count = 0
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                flag = True
                swap_count += 1
                a[j], a[j + 1] = a[j + 1], a[j]
        if flag == False: break
    return a, swap_count, a[0], a[-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    # a = [int(i) for i in input().strip().split(" ")]
    a, swap_count, first_element, last_element = bubble_sort(a, n)
    print("Sorted array is {}.".format(a))
    print("Array is sorted in {} swaps.".format(swap_count))
    print("First Element: {}".format(first_element))
    print("Last Element: {}".format(last_element))
