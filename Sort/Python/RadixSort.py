# Code taken from http://www.geekviewpoint.com/python/sorting/radixsort
# TO-DO: refactor for negative values too
class RadixSort:

    def radix_sort(self, array):
        RADIX = 10
        max_length = False
        tmp, placement = -1, 1

        while not max_length:
            max_length = True
            # declare and initialize buckets
            buckets = [list() for _ in range(RADIX)]

            # split aList between lists
            for i in array:
                tmp = i / placement
                buckets[int(tmp % RADIX)].append(i)
                if max_length and tmp > 0:
                    max_length = False

            # empty lists into aList array
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    array[a] = i
                    a += 1

            # move to next digit
            placement *= RADIX

        return array

if __name__ == '__main__':
    rs = RadixSort()
    array = [18, 5, 100, 3, 1, 19, 6, 0, 7, 4, 2]
    print(rs.radix_sort(array))