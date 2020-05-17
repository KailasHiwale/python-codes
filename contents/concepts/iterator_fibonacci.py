class Fibonacci:
	"""Class to find fibonacci series for n numbers using iterator."""
	def __init__(self, n):
		self.n = n
		self.count = 0
		self.n1 = 0
		self.n2 = 1
		self.nth = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.count < self.n:
			res = self.nth
			self.nth = self.n1 + self.n2
			self.n1 = self.n2
			self.n2 = self.nth
			self.count += 1
			return res
		else:
			raise StopIteration


if __name__ == '__main__':
	#1 Iterate using for loop
	print('Iterate using for loop -')
	for item in Fibonacci(10):
		print(item, end=' ')
	print('\n')

	#2 Iterate manually
	print('Iterate manually -')
	fibo = Fibonacci(4)
	# Create iterator object using __iter__() or iter().
	fi = iter(fibo)
	# Call next element using __next__() or next()
	print(fi.__next__(), end=' ')
	print(next(fi), end=' ')
	print(next(fi), end=' ')
	print(next(fi))
	print(next(fi))

		