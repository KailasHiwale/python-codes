# Factorial of a given number by iterative and recusive ways.


def factorial(n):
    """Iterative function to return factorial of a number."""
    fact = 1
    if n == 0:
        return fact
    else:
        while n > 1:
            fact = fact * n
            n -= 1
        return fact


def factorial_recursive(n):
    """Recursive function to return factorial of a number."""
    if n <= 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


# Start
if __name__ == '__main__':
    # Except number
    n = int(input("Enter positive number: "))
    
    # Factorial iterative call
    print("Factorial iterative call:")
    if n < 0:
        print("Enter positive number")
    else:
        print(factorial(n))

    # Factorial recursive call
    print("Factorial recursive call:")
    if n < 0:
        print("Enter positive number")
    else:
        print(factorial(n))
