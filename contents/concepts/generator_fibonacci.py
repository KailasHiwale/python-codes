def fibonacci(n):
	n1, n2, nth, count = 0, 1, 1, 0
	while count < n:
		yield nth
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count += 1


if __name__ == '__main__':
	#1 Iterate using for loop
	print('Iterate using for loop -')
	for item in fibonacci(10):
		print(item, end=' ')
	print('\n')

	print('Iterate manually -')
	# Create iterator object using __iter__() or iter().
	fi = fibonacci(4).__iter__()
	# Call next element using __next__() or next()
	print(fi.__next__(), end=' ')
	print(next(fi), end=' ')
	print(next(fi), end=' ')
	print(next(fi))
	print(next(fi))