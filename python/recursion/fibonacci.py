# Hint: Fibonacci Sequese n = (n-1) + (n-2), Where n is next number


def fibonacci_sequence(num):
    if num <= 1:
        return num
    else:
        return fibonacci_sequence(num - 1) + fibonacci_sequence(num - 2)


num = int(input("Enter positive number:"))

if num <= 0:
    print("Enter positive number!")
else:
    print("Fibonacci Sequence: ")
    for i in range(num):
        print(fibonacci_sequence(i), end=" ")

