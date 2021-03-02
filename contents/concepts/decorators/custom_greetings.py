#Functions returns functions

def greeting(lang):
	def custom_greetings(name):
		if lang.lower() == 'english':
			greet = 'Hello '
		elif lang.lower() == 'german':
			greet = 'Hallo '
		elif lang.lower() == 'marathi':
			greet = 'Namaskar '
		else:
			greet = 'Hi '

		return greet + name + '!!'
	return custom_greetings


# lang = input('Language: ')
# name = input('Name: ')
# greet = greeting(lang)
# print(greet(name))


def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


#1 Using function calls
def foo(x):
    print(x)


# (Pdb) g1 = greeting('Hallo')
# (Pdb) dir(g1)
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# (Pdb) g1.__name__
# 'greeting_decorator'
# (Pdb) g2 = g1(foo)
# (Pdb) g2.__name__
# 'function_wrapper'
# (Pdb) g2('10')
# Hallo, foo returns:

# Or

#  foo = greeting('Hallo')(foo)


#2 Using @ decorator
@greeting('Hallo')
def foo2(x):
	print(x)


# foo2(10)