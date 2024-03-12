import pickle as p
import os as o

class Mydes:
    def __init__(self, name="x"):
        self.name = name
        self.filepath = "E:\\test\\新建文件夹\\属性日志%s.pkl" % self.name

    def __set__(self, instance, value):
        f = open(self.filepath, "ab")
        p.dump(value,f)
        f.close()

    def __delete__(self, instance):
        del self.name
        o.remove(self.filepath)



class A:
    m = Mydes()

a = A()
a.m = 5
del a.m