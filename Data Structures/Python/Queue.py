# Simple wrapper for queues as Python's Dequeue implementation already mirrors Queues
from collections import deque


class Queue:
    def __init__(self, data=None):
        if data is not None:
            self.queue = deque([data])
        else:
            self.queue = deque([])

    def __str__(self):
        return str(self.queue)

    def add(self, data):
        self.queue.append(data)

    def pop(self):
        self.queue.popleft()


class StackQueue:
    def __init__(self):
        self.in_queue = []
        self.out_queue = []

    def enqueue(self, data):
        while not self.out_queue:
            self.in_queue.append(self.out_queue.pop())
        self.in_queue.append(data)

    def dequeue(self):
        while not self.in_queue:
            self.out_queue.append(self.in_queue.pop())
        return self.out_queue.pop()


if __name__ == '__main__':
    queue = Queue()
    queue.add(4)
    queue.add(7)
    queue.pop()
    print(queue)