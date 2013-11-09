class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

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

        if not self.tail is None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node(self, index):
        prev = None
        pointer = self.head
        i = 0

        while not pointer is None and (i < index):
            prev = pointer
            pointer = pointer.next
            i += 1

        if prev is None:
            self.head = pointer.next
        else:
            prev.next = pointer.next

    def print_list(self):
        pointer = self.head
        while not pointer is None:
            print(pointer.data, end=" ")
            pointer = pointer.next

if __name__ == '__main__':
    l_list = LinkedList()
    l_list.add_node(1)
    l_list.add_node(2)
    l_list.add_node(3)
    l_list.add_node(4)
    #l_list.print_list()
    l_list.remove_node(2)
    l_list.print_list()
