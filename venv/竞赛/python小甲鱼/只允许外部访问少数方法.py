>>> class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)

>>> class C:
    def __init__(self):
        self._x = None  # 你想声明为私有的方法和属性前加上单下划线,以提示该属性和方法不应在外部调用
    def getX(self):
        return self._x
    def setX(self, value):
        self._x = value
    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)

