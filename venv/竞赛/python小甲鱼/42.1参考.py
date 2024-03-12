class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]

a = Nstr(123456789)
print(a >> 2)
print(a << 2)