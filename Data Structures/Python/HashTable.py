# Simple wrapper for hash tables as Python's Dictionary implementation already mirrors it
from collections import deque


class HashTable:
    def __init__(self):
        self.hash_table = {}

    def __str__(self):
        return str(self.hash_table)

    def insert(self, key, value):
        self.hash_table[key] = value

    def remove(self, key):
        del self.hash_table[key]

    def find(self, key):
        self.hash_table.get(key)

    def keys(self):
        self.hash_table.keys()

if __name__ == '__main__':
    hash = HashTable()
    hash.insert('a', 1)
    hash.insert('b', 2)
    hash.insert('c', 3)
    print(hash.keys())
    hash.remove('b')
    print(hash)