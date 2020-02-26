#!/bin/python3

"""
    Stack
    -----
    A stack or LIFO (last in, first out) is an abstract data type that serves
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.
    Pseudo Code: https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29
"""

from collections import deque


class Stack(object):
    """Class to create stack"""
    def __init__(self):
        self.stack = deque()

    def __repr__(self):
        pass

    def push(self, data):
        """push element on top of the stack.
        Takes O(1) time
        """
        self.stack.append(data)

    def pop(self):
        """pop element on top of the stack.
        Takes O(1) time"""
        if self.stack:
            self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        """Return last element of stack.
        Takes O(1) time
        """
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        """Return 1 on empty and 0 on non empty
        Takes O(1) time
        """
        return not self.size()

    def size(self):
        """Return size of stack
        Takes O(1) time
        """
        return len(self.stack)


# Start
if __name__ == '__main__':
    stack_lst = Stack()
    for item in range(10):
        stack_lst.push(item)
    stack_lst.pop(1)
    stack_lst.is_empty()
    stack_lst.size()
