# Implementation from http://www.geekviewpoint.com/python/sorting/heapsort


class HeapSort:

    def moveDown(self, aList, first, last):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
                largest += 1

            # right child is larger than parent
            if aList[largest] > aList[first]:
                self.swap(aList, largest, first)
                # move down to largest child
                first = largest
                largest = 2 * first + 1
            else:
                return # force exit

    def swap(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def heap_sort(self, aList):
        # convert aList to heap
        length = len(aList) - 1
        least_parent = int(length / 2)
        for i in range(least_parent, -1, -1):
            self.moveDown(aList, i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if aList[0] > aList[i]:
                self.swap(aList, 0, i)
                self.moveDown(aList, 0, i - 1)

if __name__ == '__main__':
    hs = HeapSort()
    array = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(hs.heap_sort(array))