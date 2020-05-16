# Module to swap two givan numbers.

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Original:\nx={}\ny={}".format(x, y))

# Method 1: Swap using python inbuilt feature
x, y = 10, 7
x, y = y, x
print("Method 1:\nx={}\ny={}".format(x, y))

# Method 2: Swap using third variable
x, y = 10, 7
temp = x
x = y
y = temp
print("Method 2:\nx={}\ny={}".format(x, y))

# Method 3: Swap without using third variable and python inbuilt feature
x, y = 10, 7
x = x + y
y = x - y
x = x - y
print("Method 3:\nx={}\ny={}".format(x, y))
