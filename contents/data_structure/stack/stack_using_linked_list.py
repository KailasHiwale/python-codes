#!/bin/python3


class StackNode:
    """Linked list Node for Stack."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Return the string representation of the data."""
        return repr(self.data)


class Stack:
    """Class for Stack operations."""
    def __init__(self):
        """Function initialises head node.
        Takes O(1) time.
        """
        self.head = None

    def push(self, data):
        """Add the element last of the stack."""
        new_node = StackNode(data=data, next=self.head)
        self.head = new_node
        print("{} pushed to the stack.".format(data))

    def pop(self):
        """Remove element from the stack."""
        if self.is_empty():
            return "pop from empty stack"
        temp = self.head
        self.head = self.head.next
        return temp.data

    def is_empty(self):
        """Check if stack is empty."""
        return True if self.head is None else False

    def peak(self):
        """Return top element of the stack."""
        if self.is_empty():
            return
        else:
            return self.head.data


# Start
if __name__ == '__main__':
    stack_node = Stack()
    for i in range(5):
        stack_node.push(i)
    stack_node.pop()
    stack_node.is_empty()
    stack_node.peak()
