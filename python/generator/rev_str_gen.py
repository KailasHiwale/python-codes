def rev_str(st):
    for i in range(len(st) - 1, - 1, - 1):
        yield st[i]


for ch in rev_str(input("Enter string: ")):
    print(ch, end="")
