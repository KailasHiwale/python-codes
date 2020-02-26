#!/bin/python3


def pcount(input_str=None):
    """Funtion returns number of palindrome string"""
    try:
        replace_char = [".", ",", ":", "?"]
        for ch in replace_char:
            input_str = input_str.replace(ch, "")
        lst = input_str.split(" ")
        count = len([st for st in lst if st[::-1] == lst[lst.index(st)]])
        return count
    except Exception as e:
        return e


if __name__ == '__main__':
    input_str = input("Enter string\n")
    print(pcount(input_str))
