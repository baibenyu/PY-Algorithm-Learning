class Centigrade:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value * 1.8 + 32)

    def __delete__(self, instance):
        self.fdel(instance)


class Fahrenheit:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, (value - 32) / 1.8)

    def __delete__(self, instance):
        self.fdel(instance)


class Temperature():
    def __init__(self, value=0):
        self.temperature = value

    def get(self):
        return self.temperature

    def set(self, value):
        self.temperature = value

    def delete(self):
        del self.temperature

    c = Centigrade(get, set, delete)
    f = Fahrenheit(get, set, delete)


t = Temperature()
print(t.c)
t.c = 20
print(t.c)
t.f = 20
print(t.f)
del t.c

