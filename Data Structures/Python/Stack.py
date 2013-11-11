# Simple wrapper for stacks as Python's List implementation already mirrors Stacks


class Stack:
    def __init__(self, data=None):
        if data is not None:
            self.stack = [data]
        else:
            self.stack = []

    def __str__(self):
        return str(self.stack)

    def add(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

if __name__ == '__main__':
    stack = Stack()
    stack.add(4)
    stack.add(7)
    stack.pop()
    print(stack)