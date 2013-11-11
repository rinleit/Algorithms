class Strings:

    def sub_string(self, a, b):
        return a in b

    def a_to_i(self, string):
        sum, neg = 0, False

        if string[0] == "-":
            neg = True
            string = string[1:]

        for i in range(len(string)):
            sum = (sum * 10) + int(string[i])

        if neg:
            return sum * -1
        else:
            return sum

    def reverse_word(self, word):
        return word[::-1]

if __name__ == '__main__':
    strs = Strings()
    print(strs.sub_string("bat", "abate"))
    print(strs.a_to_i("-345623452345"))
    print(strs.reverse_word("this is a sentence"))