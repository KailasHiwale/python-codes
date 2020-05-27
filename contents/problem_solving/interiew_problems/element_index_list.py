"""
:Created on: May 27th, 2020
:Company: IBM
:Problem statement: Program to get list of indexes for an element.
"""


def element_indx(lst, item):
	res = []
	try:
		for i in lst:
			if i == item:
				res.append(lst.index(i))
				ind = lst.index(i)
				lst.pop(ind)
				lst.insert(ind, None)
		return res
	except ValueError as e:
		return None


lst = [1, 2, 1, 3, 4, 5, 1]
item = int(input())
res = element_indx(lst, item)

if res:
	print(res)
else:
	print('not found')

# Input: 1
# Output: [0, 2, 6]
