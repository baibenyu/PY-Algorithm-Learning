class Word(str):
    def __new__(cls,word):
        if " " in word:
            print("字符中含空格,仅取出第一个空格前所有字符")
            word = word[:word.index(" ")]
        return str.__new__(cls,word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return  len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


w1 = Word('abcd')
w2 = Word('abca vsdv')
if w1 >= w2:
    print(True)