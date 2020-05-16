#!/bin/python3

"""
NOTE
----
queue.PriorityQueue class implements heapq internally and shares
same time and space complexities. The difference is that
PriorityQueue is synchronized and provides locking semantics to
support multiple concurrent producers and consumers.

https://dbader.org/blog/priority-queues-in-python
"""

from queue import PriorityQueue


class HeapQueue(object):
    """Class for Priority Queue"""
    def __init__(self):
        self.lst = PriorityQueue()

    def enqueue(self, data):
        """Add element to the Priority Queue."""
        self.lst.put(data)
        print("{} added".format(data))

    def dequeue(self):
        """Remove element from the Priority Queue."""
        return "{} removed".format(self.lst.get())


if __name__ == '__main__':
    pq = HeapQueue()
    westeros = [(2, "Stark"), (1, "Baratheon"), (3, "Lanister")]
    for house in westeros:
        pq.enqueue(house)
    print(pq.dequeue())
