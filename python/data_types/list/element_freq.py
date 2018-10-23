def element_frequency(li):
    """Function to find frequency of each element of list"""
    di = {}
    for i in li:
        di[i] = li.count(i)
    return di


li = input("Enter list i.e 1,2,3,1: ").split(",")
di = element_frequency(li)
print("Element Frequency: ")
for key, value in di.items():
    print("{}: {}".format(key, value))
