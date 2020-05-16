#!/bin/python3

"""
NOTE
----
Only suitable when there will be few insertions into the priority queue.

https://dbader.org/blog/priority-queues-in-python
"""


class PQueue(object):
    """Class for Priority Queue"""
    def __init__(self):
        self.lst = []

    def enqueue(self, data):
        """Add element to the Priority Queue."""
        self.lst.append(data)
        self.lst.sort(reverse=True)
        print("{} added".format(data))

    def dequeue(self):
        """Remove element from the Priority Queue."""
        return "{} removed".format(self.lst.pop())


if __name__ == '__main__':
    pq = PQueue()
    westeros = [(2, "Stark"), (1, "Baratheon"), (3, "Lanister")]
    for house in westeros:
        pq.enqueue(house)
    print(pq.lst)
    print(pq.dequeue())
    print(pq.lst)
