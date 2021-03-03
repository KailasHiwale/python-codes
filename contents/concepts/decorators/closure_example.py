def greet(name):
	def wrap():
		return 'Hallo ' + name + '!!'
	return wrap


'''
>>> g = greet('John')
>>> g()
'Hallo John!!'
>>> greet.__name__
'greet'
>>> del greet
>>> greet.__name__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'greet' is not defined
>>> g()
'Hallo John!!'
'''


def calculate(ops):
	def operation(first=0, second=0):
		if ops.lower() == 'multiply':
			return first * second
		elif ops.lower() == 'divide':
			return first / second
		else:
			return first + second
	return operation

import pdb;pdb.set_trace()

'''
(Pdb) x = calculate('multiply')
(Pdb) x(10, 20)
200
(Pdb) del calculate
(Pdb) x(10, 12)
120
(Pdb)
'''
