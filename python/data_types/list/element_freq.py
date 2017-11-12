li = [2, 4, 2, 1, 5, 3, 2, 2, 6]
di = {}

for i in li:
    di[i] = li.count(i)

print("Element Frequency: ")
for key, value in di.items():
    print("{}: {}".format(key, value))
