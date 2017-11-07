from __future__ import print_function

num = int(input("Enter positive number: "))
n1, n2, count = 0, 1, 0

if num <= 0:
    print("Enter +ve number: ")
else:
    print("Fibonacci Sequence:")
    while count <= num:
        print(n1, end=", ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
