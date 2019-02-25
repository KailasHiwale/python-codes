#!/bin/python3

"""
Note
----
Built in dict has better performance. It is versatile and optimized
dictionary implementation that’s built directly into the core language.
"""

from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType

"""
1. Built in dict type.
Python dictionaries are based on a well-tested and finely tuned
hash table implementation that provides the performance
characteristics you’d expect: O(1) time complexity for lookup,
insert, update, and delete operations in the average case.
"""
print("\n\n1. Built in dict type.")

houses = {
    'House Arryn': 'John Arryn',
    'House Lanister': 'Tywin Lanister',
}

houses["House Lanister"] = "Tywin Lanister"

for house, lord in houses.items():
    print(house + ": " + lord)

"""
2. collections.OrderedDict –
A dictionary subclass that remember the insertion order of keys
"""

print("\n\n. collections.OrderedDict")
houses_ord = OrderedDict(House_Arryn="John Arryn",)
houses_ord["House Lanister"] = "Tywin Lanister"
print(houses_ord)
houses_ord["House Stark"] = "Ned Stark"
print(houses_ord)
for house, lord in houses_ord.items():
    print(house + ": " + lord)

"""
3. collections.defaultdict –
A Dictinory subclass return default values for missing keys
"""
print("\n\n3. collections.defaultdict")
dd = defaultdict(list)
# Accessing a missing key creates it and initializes it
# using the default factory, i.e. list() in this example:
dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

print(dd["dogs"])

"""
4. collections.ChainMap –
Search multiple dictionaries as a single mapping
"""
print("\n\n4. collections.ChainMap")
dict1 = {"John": 4, "Snow": 4}
dict2 = {"Ned": 3, "Stark": 5}
cm = ChainMap(dict1, dict2)
try:
    print(cm["John"])
    print(cm["Ned"])
    print(cm["Nedd"])
except KeyError as e:
    print(e)

"""
5. types.MappingProxyType –
A wrapper for making read-only dictionaries
"""
print("\n\n5. collections.ChainMap")
read_only = MappingProxyType({"John": 4, "Snow": 4})
try:
    print(read_only["John"])
    read_only["John"] = "Rambo"
except TypeError as e:
    print(e)
