li = [2, 4, 1, 2, 11, 10, 1, 2, 5]


def sort_list_asc(li):
    li2 = []
    while len(li) > 0:
        max, i = li[0], 1
        for i in li:
            if i >= max:
                max = i
        li2.append(max)
        li.remove(max)
    print("Dscending order: \n", li2)


sort_list_asc(li)

li = [2, 4, 1, 2, 11, 10, 1, 2, 5]


def sort_list_dsc(li):
    li2 = []
    while len(li) > 0:
        min, i = li[0], 1
        for i in li:
            if i <= min:
                min = i
        li2.append(min)
        li.remove(min)
    print("Ascending order: \n", li2)


sort_list_dsc(li)
