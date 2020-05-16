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

    def print_data(self):
        """Function to print linked list data."""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def prepend(self, data):
        """Insert new node at the beginning.
        Time complexity O(1).
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """Insert new node at the end of the linked list.
        Time complexity O(n).
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(data=data)

    def search(self, data):
        """Search for the first element's matching `data` with
        given `data` value. Return element or None if not found.
        Time compexity O(n)
        """
        current = self.head
        while current and current.data != data:
            current = current.next
        return current    # Will return None if not found

    def remove(self, data):
        """Remove the first occurrance of `data` value in linked list
        Time complexity O(n)
        """
        # Find node and keep reference to the previous node.
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        # Unlink the target node
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        current = self.head
        prev_node = None
        next_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node


if __name__ == '__main__':
    # Instantiate the head or start with empty linked list
    linked_lst = LinkedList()

    # Creates the node
    linked_lst.head = ListNode(3)
    second = ListNode(4)
    third = ListNode(1)

    # Linked the nodes one by one.
    # Next of current node refers to the next node address.
    linked_lst.head.next = second
    second.next = third

    linked_lst.get_data()
    linked_lst.prepend(44)
    linked_lst.append(50)
    linked_lst.search(44)
    linked_lst.remove(50)


