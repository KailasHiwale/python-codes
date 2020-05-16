#!/bin/python3


class ListNode:
    """Node for singly linked list."""
    def __init__(self, data=None, next=None):
        """Function to initialise the node object."""
        self.data = data
        self.next = next

    def __repr__(self):
        """Return the string representation of the data."""
        return repr(self.data)


class LinkedList:
    """Create new singly linked list."""
    def __init__(self):
        """Function initialises head node.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'


if __name__ == '__main__':
    # Instantiate the head or start with empty linked list
    linked_lst = LinkedList()

    # Creates the node
    linked_lst.head = ListNode(3)
    second = ListNode(4)
    third = ListNode(1)

    # Linked the nodes one by one.
    # Next of current node refers to the next node.
    linked_lst.head.next = second
    second.next = third
