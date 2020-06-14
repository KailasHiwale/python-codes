# with inbuilt feature
>>> st = 'westeros'
>>> st[::-1]
'saliak'

# Without using inbuilt feature
>>> st = 'westeros'
>>> rst = ''
>>> for i in st:
...     rst = i + rst
... 
>>> rst
'saliak'
>>> 