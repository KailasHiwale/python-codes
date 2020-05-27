"""
:Created on: May 27th, 2020
:Company: IBM
:Problem statement: Program to extract version number for each element of a list.
"""


def os_version(lst):
	"""Function extracts redhat version number for each element of a list."""
	return [item.split(' ')[-1] for item in lst]


if __name__ == '__main__':
	lst = ['Redhat 6.5', 'Redhat 6.6', 'Redhat 6.7', 'Redhat 7.1-beta1', 'Redhat 7.2', 'Redhat 7.3']
	for version in os_version(lst):
		print(version)


# Input: lst
# Output: ['6.5', '6.6', '6.7', '7.1-beta1', '7.2', '7.3']


