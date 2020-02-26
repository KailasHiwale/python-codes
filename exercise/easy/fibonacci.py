# Module to calculate the fibonacci series for given limit.

from __future__ import print_function


def fibonacci_recursive(n):
    """Recursive function return fibonacci series"""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci(n):
    """Recursive function return fibonacci series"""
    n1, n2, count, nth = 1, 0, 0, 1
    if n <= 1:
        return n
    else:
        while count < n:
            print(nth, end="  ")
            nth = n1 + n2
            n2 = n1
            n1 = nth
            count += 1
        return " "


# Start
if __name__ == '__main__':
    # Except the limit for fibonacci series
    nterm = int(input("Enter a number:\n"))

    # Fibonacci recursive call
    print("\nFibonacci recursive call:")
    if nterm <= 0:
        print("Fibonacci series not possible for {}".format(nterm))
    else:
        for i in range(1, nterm + 1):
            print(fibonacci_recursive(i), end="  ")
        print("\n")

    # Fibonacci iterative call
    print("Fibonacci iterative call:")
    if nterm <= 0:
        print("Fibonacci series not possible for {}".format(nterm))
    else:
        print(fibonacci(nterm))