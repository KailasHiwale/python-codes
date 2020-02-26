#!/bin/python3


class QueueNode:
    """Linked list Node for Stack."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        """Return the string representation of the data."""
        return repr(self.data)


class Queue:
    """Class to create queue"""
    def __init__(self):
        """Function to initialise the node object."""
        self.front = None
        self.rear = None

    def __repr__(self):
        pass

    def enqueue(self, data):
        if not self.rear:
            self.rear = self.front = QueueNode(data=data)
            print("{} added to rear end of the queue.".format(data))
            return
        self.rear = QueueNode(data=data, next=self.rear)
        print("{} added to rear end of the queue.".format(data))


    def dequeue(self):
        temp, previous, data = self.rear, None, None
        if not self.rear:
            return data
        while temp.next:
            previous = temp
            temp = temp.next
        if not previous:
            data = temp.data
            temp.next = None
        else:
            self.front = temp
            data = temp.data
            previous.next = None

        return data

    def is_empty(self):
        """Return True on empty and False on non empty"""
        return True if self.head is None else False


# Start
if __name__ == '__main__':
    que = Queue()
    que.is_empty()
    westeros = [
        "House Stark",
        "House Tully",
        "House Arryn"
        "House Baratheon",
        "House Lanister",
        "House Tyrell",
        "House Martell", ]
    for house in westeros:
        que.enqueue(house)
    que.dequeue()
    que.is_empty()

