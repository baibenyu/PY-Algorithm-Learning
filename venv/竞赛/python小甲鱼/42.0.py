class Nstr(str):
    def __sub__(self, other):
        if other in self:
            return self.replace(other,"")
        else:
            print("不含有%s字符串" % other)

a = Nstr(123456123456)
b = Nstr(13)
print(a - b)