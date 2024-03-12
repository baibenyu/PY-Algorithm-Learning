class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.name

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.name = value

    def __delattr__(self, instance):
        print("正在删除变量：", self.name)
        print("┗|｀O′|┛ 嗷~~这个变量没法删除~")


class A:
    m = MyDes(1, 2)

a =A()
a.m
a.m = 5
a.m
del a.m
