#!/bin/python3

"""
NOTE
----
heapq is a good choice for implementing priority queues in Python.
This supports insertion and extraction of the smallest element in
O(log n) time.

https://dbader.org/blog/priority-queues-in-python
"""

import heapq


class HeapQueue(object):
    """Class for Priority Queue"""
    def __init__(self):
        self.lst = []

    def enqueue(self, data):
        """Add element to the Priority Queue."""
        heapq.heappush(self.lst, data)
        print("{} added".format(data))

    def dequeue(self):
        """Remove element from the Priority Queue."""
        return "{} removed".format(heapq.heappop(self.lst))


if __name__ == '__main__':
    pq = HeapQueue()
    westeros = [(2, "Stark"), (1, "Baratheon"), (3, "Lanister")]
    for house in westeros:
        pq.enqueue(house)
    print(pq.lst)
    print(pq.dequeue())
    print(pq.lst)
