class Strings:

    def sub_string(self, a, b):
        return a in b

if __name__ == '__main__':
    strs = Strings()
    print(strs.sub_string("bat", "abate"))