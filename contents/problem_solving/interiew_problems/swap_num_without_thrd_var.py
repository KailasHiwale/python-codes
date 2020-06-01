"""
:Created on: May 27th, 2020
:Company: Infogain
"""

a = 10
b = 18
print('Original:\na: {}, b: {}'.format(a, b))
a = a + b
b = a - b
a = a - b
print('After swap:\na: {}, b: {}'.format(a, b))