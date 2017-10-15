# Hint: 5! = 5 * 4 * 3 * 2 * 1, 0! = 1
def factorial(num):
    '''Function for factorial of number using recursion'''
    if num < 0:
        print("Enter positive number!")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print("Factorial=", factorial(int(input("Enter zero or positive number: "))))
