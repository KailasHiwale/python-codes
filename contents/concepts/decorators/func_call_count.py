def func_call_count(func):
	def call_count(*args, **kwargs):
		call_count.count += 1
		return func(*args, **kwargs)
	call_count.count = 0
	return call_count


@func_call_count
def add(a=0, b=0):
	return a+b


@func_call_count
def mul(a=0, b=0, c=0):
	return a*b*c


print(add.count)
print(mul.count)
for i in range(10):
	if i % 2:
		print('if block: ', i)
		add(i, i+1)
	else:
		print('else block: ', i)
		mul(i, i+1, i+2)
print(add.count)
print(mul.count)
