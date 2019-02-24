#!/bin/python3

"""
Note
----
`queue` implementation in the Python standard library is synchronized
and provides locking semantics to support multiple concurrent
producers and consumers.

Usefull for parallel computing.
"""

from queue import Queue


class Que(object):
    """Class to create Queue"""
    def __init__(self):
        self.queue = Queue()

    def __repr__(self):
        pass

    def enqueue(self, data):
        """Add an element to the Queue."""
        self.queue.put(data)

    def dequeue(self):
        """Remove an element from the Queue."""
        if self.queue:
            self.queue.get()
        else:
            return "removing from an empty Queue"

    def front(self):
        """Return the first element of the Queue."""
        q = self.queue
        que_lst = [q.get() for i in range(q.qsize())] if q.qsize() else None
        if que_lst:
            for item in que_lst:
                q.put(item)
        return que_lst[0] if que_lst else None

    def rear(self):
        """Return last element of Queue."""
        q = self.queue
        que_lst = [q.get() for i in range(q.qsize())] if q.qsize() else None
        if que_lst:
            for item in que_lst:
                q.put(item)
        return que_lst[0] if que_lst else None

    def is_empty(self):
        """Return 1 on empty and 0 on non empty"""
        return self.queue.empty()

    def size(self):
        """Return size of queue
        Takes O(1) time
        """
        return self.queue.qsize()


# Start
if __name__ == '__main__':
    queue_lst = Que()
    for item in range(10):
        queue_lst.enqueue(item)
    queue_lst.dequeue(1)
    queue_lst.rear()
    queue_lst.front()
    queue_lst.is_empty()
    queue_lst.size()
