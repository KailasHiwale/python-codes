# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)


# ========================================================

# Program to double each item in a list using map()

my_list2 = [1, 5, 4, 6, 8, 11, 3, 12]

new_list2 = list(map(lambda x: x * 2 , my_list2))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list2)