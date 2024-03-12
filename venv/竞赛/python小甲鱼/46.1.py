import time as t


class Mydes:
    def __init__(self, initial = None, name=None, time=None, file_path='E:\\test\\新建文件夹\\修改日志.txt'):
        self.val = initial
        self.name = name
        self.file_path = file_path
        self.time = time

    def __get__(self, instance, owner):
        with open(self.file_path, "a+") as f:
            self.time = str(t.localtime())
            f.write("在 %s 的时候对变量 %s 进行了访问" % (self.time, self.name))
            return self.val

    def __set__(self, instance, value):
        with open(self.file_path, "a+") as f:
            self.time = str(t.localtime())
            f.write("在 %s 的时候对变量 %s 进行了修改.修改后的值为%s" % (self.time, self.name, value))
        self.val = value


class A:
    m = Mydes()


a = A()
print(a.m)
a.m = 5
