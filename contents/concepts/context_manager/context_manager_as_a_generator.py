'''
Let’s dissect this method a little.

- Python encounters the yield keyword. Due to this it creates a generator instead of a normal function.
- Due to the decoration, contextmanager is called with the function name (openfile) as its argument.
- The contextmanager decorator returns the generator wrapped by the GeneratorContextManager object.
- The GeneratorContextManager is assigned to the openfile function. Therefore, when we later call the
openfile function, we are actually calling the GeneratorContextManager object.
'''


from contextlib import contextmanager


@contextmanager
def openfile(file_name):
	file = open(file_name, 'w')
	try:
		yield file
	finally:
		file.close()


with openfile('text.txt') as file:
	file.write('Hallo!!')