st = input("Enter string: ")


def word_count(st):
    li = st.split(" ")
    return len(li)


print("Word count: ", word_count(st))
