class Strings:

    def sub_string(self, string, substring):
        if len(string) == 0 and len(substring) == 0:
            return True

        if len(string) > len(substring):
            return False

        for i in range(len(string)):
            mismatch = False
            for j in range(len(substring)):
                print("Starting..." + str(i) + str(j))
                if string[i+j] != substring[j]:
                    print("String:" + string[i+j] + " Substring:" + substring[j])
                    mismatch = True
                    print("Breaking..." + str(i) + str(j))
                    break

            if not mismatch:
                return True

        return False

if __name__ == '__main__':
    strs = Strings()
    print(strs.sub_string("bat", "abate"))