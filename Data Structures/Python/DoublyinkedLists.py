class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                break
            current = current.next