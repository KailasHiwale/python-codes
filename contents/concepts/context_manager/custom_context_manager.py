'''
Our __exit__ method accepts three arguments. They are required by every __exit__ method which is a part of a Context Manager class.
Internal working:
1. The with statement stores the __exit__ method of the File class.
2. __enter__ method of the File class gets called. __enter__ method opens the file and returns it
3. The with statement calls the stored __exit__ method and __exit__ method closes the file.

type, value and traceback arguments of the __exit__ method allow exit method to decide how to close the file if exception occures.
It return True, if exception handled gracefully else it raises appropreate exception.

with File('demo.txt', 'w') as file:
    file.xyz('Hallo!')

output:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'file' object has no attribute 'xyz'

'''


class FileOpen(object):
	def __init__(self, file_name, method):
		self.file_obj = open(file_name, method)

	def __enter__(self):
		return self.file_obj

	def __exit__(self, type, value, traceback):
		self.file_obj.close()


with FileOpen('test.txt', 'w') as file:
	file.write('Hallo!!')

with File('demo.txt', 'w') as file:
    file.xyz('Hallo!')