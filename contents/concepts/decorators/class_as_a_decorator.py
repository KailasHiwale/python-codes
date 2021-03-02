#Example 1
class Greet:
	def __init__(self, func):
		self.func = func

	def __call__(self):
		print('Inside __call__')
		self.func()


@Greet
def greetings():
	print('Hallo!!')

print('Greet using class decorators:')
greetings()


#Example 2
class Fibonacci:

    def __init__(self):
        self.num = dict()

    def __call__(self, n):
    	if n == 0:
    		self.num[0] = 0
    	elif n == 1:
    		self.num[1] = 1
    	else:
    		self.num[n] = self.__call__(n-1) + self.__call__(n-2)

    	return self.num[n]


print('Fibonacci series using class decorators:')
fib = Fibonacci()
for i in range(10):
	print(fib(i), end=', ')