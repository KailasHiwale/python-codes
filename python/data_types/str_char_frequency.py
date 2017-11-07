st = input("Enter string: ")
di = {}
for i in st:
    di[i] = st.count(i)

print("Frequency count of character in given string:")
for key, value in di.items():
    print("{}: {}".format(key, value))
