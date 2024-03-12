class Nstr():

    def __init__(self,args=""):
        self.asc = 0
        for each in args:
            self.asc += ord(each)


    def __add__(self, other):
        return self.asc+other.asc

    def __sub__(self, other):
        return self.asc-other.asc

    def __mul__(self, other):
        return self.asc*other.asc

    def __truediv__(self, other):
        return self.asc/other.asc

    def __floordiv__(self, other):
        return self.asc // other.asc

a = Nstr("a")
b = Nstr("b")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)