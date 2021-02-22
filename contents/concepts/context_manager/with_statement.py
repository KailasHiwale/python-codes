'''
Context managers allow you to allocate and release resources precisely when you want to.

Example:
with open('test.txt', 'w') as file:
    file.write('Hallo!!')

The above code opens the file, writes some data to it and then ensures file gets closed.
If any error occures while writing data context manager handles closing of file. Above is equivalent to -

file = open('test.txt', 'w')
try:
    file.write('Hallo!!')
finally:
    file.close()
'''