# Desc1
# Sort list without using any inbuilt function in dscending order
li = [4, 1, 2, 1, 7, 2, 9, 0]


def sort_list_dsc(li):
    li2 = []
    while len(li) > 0:
        max, i = li[0], 1
        for i in li:
            if i >= max:
                max = i
        li2.append(max)
        li.remove(max)
    print("Dscending order: \n", li2)


sort_list_dsc(li)


# Desc2
# Sort list without using any inbuilt function in dscending order
li2 = [4, 1, 2, 1, 7, 2, 9, 0]


def sort_list_dsc_2(li2):
    count, m = 0, 0

    for i in li2:
        count += 1

    while m < count:
        n = m + 1
        while n < count:
            if li2[n] >= li2[m]:
                li2[m], li2[n] = li2[n], li2[m]
            n += 1
        m += 1

    print("Dscending order2: \n", li2)


sort_list_dsc_2(li2)


# Asc1
# Sort list without using any inbuilt function in ascending order
li = [4, 1, 2, 1, 7, 2, 9, 0]


def sort_list_asc(li):
    li2 = []
    while len(li) > 0:
        min, i = li[0], 1
        for i in li:
            if i <= min:
                min = i
        li2.append(min)
        li.remove(min)
    print("Ascending order: \n", li2)


sort_list_asc(li)

# Asc2
# Sort list without using any inbuilt function in ascending order
li2 = [4, 1, 2, 1, 7, 2, 9, 0]


def sort_list_asc_2(li2):
    count, m = 0, 0

    for i in li2:
        count += 1

    while m < count:
        n = m + 1
        while n < count:
            if li2[n] <= li2[m]:
                li2[m], li2[n] = li2[n], li2[m]
            n += 1
        m += 1

    print("Ascending order2: \n", li2)


sort_list_asc_2(li2)
