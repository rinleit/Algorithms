def odd_man_out(array):
    odd = 0
    for num in array:
        odd ^= num

    return odd

if __name__ == '__main__':
    print(odd_man_out([1, 1, 2, 2, 3, 3, 4, 5, 5]))
