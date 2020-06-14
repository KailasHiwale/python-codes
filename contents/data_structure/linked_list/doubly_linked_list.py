#!/bin/python3


class ListNode:
    """Node for doubly linked list"""
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        """Return the string representation of the data."""
        return repr(self.data)


class LinkedList:
    """Create new doubly linked list."""
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

    def print_data(self):
        """Function to print linked list data."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def prepend(self, data):
        """Insert new node at the beginning.
        Time complexity O(1)
        """
        new_head = ListNode(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def append(self, data):
        """Insert the new node at the end of the linked list.
        Time complexity O(n)
        """
        if not self.head:
            self.head = ListNode(data=data)
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(data=data, prev=current)

    def search(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        return current  # Return None if not found

    def remove_node(self, node):
        """Unlink the node
        Time complexity O(n)
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.next = None
        node.prev = None

    def remove(self, data):
        """Remove the first occurance of data.
        Time complexity O(n)
        """
        element = self.search(data)
        if not element:
            return
        self.remove_node(element)

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        current = self.head
        prev_node = None
        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev
        self.head = prev_node.prev


if __name__ == '__main__':
    linked_lst = LinkedList()
    linked_lst.prepend(10)
    linked_lst.prepend(11)
    linked_lst.append(20)
    linked_lst.append(21)
    linked_lst.print_data()
    element = linked_lst.search(10)
    linked_lst.remove_node(element)
    linked_lst.remove(10)
    linked_lst.reverse()
