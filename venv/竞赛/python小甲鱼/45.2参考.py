class Counter:
    def __init__(self):
        super().__setattr__('counter', 0)

    def __setattr__(self, name, value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(name)


c = Counter()
c.x = 1
print(c.counter)
c.y = 1
c.z = 1
print(c.counter)
del c.x
print(c.counter)
