#!/bin/python3/


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
