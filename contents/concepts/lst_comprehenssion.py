# list comprehenssion using dictionary
>>> ftree={'stark': ['Ned', 'john'], 'lannister': ['tywin', 'tyrian']}
>>> [(house, members) for house, members in ftree.items()]
[('stark', ['Ned', 'john']), ('lannister', ['tywin', 'tyrian'])]
>>>

# Nested list comprehenssion to check combination
>>> [(i, j) for j in range(3) for i in range(3)]
[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]