def is_valid(func):
	def check(num):
		if type(num) == int and num >= 0:
			return func(num)
		else:
			raise Exception('Invalid number')
	return check

@is_valid
def factorial(num):
	if num == 1 or num == 0:
		return 1
	else:
		return num * factorial(num - 1)


print(factorial(5))

