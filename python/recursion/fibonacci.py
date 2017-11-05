# Hint: Fibonacci Sequese Fn = F(n-1) + F(n-2), Where Fn is next number
from __future__ import print_function


def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


num = int(input("Enter positive number:"))

if num <= 0:
    print("Enter positive number!")
else:
    print("Fibonacci Sequence: ")
    for i in range(num):
        print(fibonacci_sequence(i), end=" ")


