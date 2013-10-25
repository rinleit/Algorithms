class BinarySearch:

    def _bin_search(self, array, key, left, right):
        if right < left:
            return -1

        mid = (left + right) // 2

        if key > array[mid]:
            return self._bin_search(array, key, mid + 1, right)
        elif key < array[mid]:
            return self._bin_search(array, key, left, mid - 1)
        else:
            return mid

    def binary_search(self, array, key):
        return self._bin_search(array, key, 0, len(array) - 1)

if __name__ == '__main__':
    bs = BinarySearch()
    a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 42, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
         28657, 46368, 75025, 121393, 196418, 317811]
    print(bs.binary_search(a, 42))

