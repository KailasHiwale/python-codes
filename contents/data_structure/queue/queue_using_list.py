#!/bin/python3

"""
Note
----
Using list as queue is not ideal from a performance perspective.
Lists are quite slow for this purpose because inserting or deletingan
element at the beginning requires shifting all of the other elements by
one, requiring O(n) time.

Can be used if you're dealing with small number of elements only.
"""


class Queue(object):
    """Class to create queue"""
    def __init__(self):
        self.queue = []

    def __repr__(self):
        pass

    def enqueue(self, data):
        """Add an element at rear of the queue.
        Takes O(1) time
        """
        self.queue.append(data)

    def dequeue(self):
        """Remove an element from front of the queue.
        Takes O(n) time"""
        if self.queue:
            self.queue.pop(0)
        else:
            raise IndexError("pop from an empty queue")

    def front(self):
        """Return the first element of the queue."""
        return self.queue[0] if self.queue else None

    def rear(self):
        """Return last element of queue."""
        return self.queue[-1] if self.queue else None

    def is_empty(self):
        """Return 1 on empty and 0 on non empty"""
        return not self.size()

    def size(self):
        """Return size of queue
        Takes O(1) time
        """
        return len(self.queue)


# Start
if __name__ == '__main__':
    queue_lst = Queue()
    for item in range(10):
        queue_lst.enqueue(item)
    queue_lst.dequeue(1)
    queue_lst.rear()
    queue_lst.front()
    queue_lst.is_empty()
    queue_lst.size()
