# Simple wrapper for stacks as Python's Dequeue implementation already mirrors Queues
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

if __name__ == '__main__':
    queue = Queue()
    queue.add(4)
    queue.add(7)
    queue.pop()
    print(queue)