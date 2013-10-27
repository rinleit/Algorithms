class MergeSort:

    def _merge(self, left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def merge_sort(self, array):
        if len(array) < 2:
            return array

        mid = len(array) // 2
        left = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])

        return self._merge(left, right)

if __name__ == '__main__':
    ms = MergeSort()
    array = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(ms.merge_sort(array))