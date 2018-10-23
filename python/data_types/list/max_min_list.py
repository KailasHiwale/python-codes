# Max/Min element in the list without using any inbuilt function
li = [2, 4, 1, 2, 11, 10, 1, 2, 5]


def max_min(li):
    """
    Function to find max/min element in the list without
    using any inbuilt function.
    """
    max, min, i = li[0], li[0], 1
    for i in li:
        if i >= max:
            max = i
        elif i <= min:
            min = i
    print("Max: {} \nMin: {}".format(max, min))


max_min(li)
