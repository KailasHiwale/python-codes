#!/bin/python3

"""
Note
----
The deque class implements a double-ended queue that supports adding and
removing elements from either end in O(1) time. But poor O(n) performance
for randomly accessing elements in the middle of the queue.

collections.deque is great default choice for general purpose queue.
"""

from collections import deque


class Queue(object):
    """Class to create queue"""
    def __init__(self):
        self.queue = deque()

    def __repr__(self):
        pass

    def enqueue(self, data):
        """Add an element to rear end of the queue.
        Takes O(1) time
        """
        self.queue.append(data)

    def dequeue(self):
        """Remove an element from front of the queue.
        Takes O(n) time"""
        if self.queue:
            self.queue.popleft()
        else:
            raise IndexError("pop from an empty deque")

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
