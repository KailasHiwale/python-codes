st = input("Enter string: ")

li = st.split(" ")
di = {}

for i in li:
    di[i] = li.count(i)

print("Frequency of words: ")

for key, value in di.items():
    print("{}: {}".format(key, value))
