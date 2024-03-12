# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/1/18 17:29'

class Person:

    def __del__(self):
        print("销毁对象{0}".format(self))


p1 = Person()
p2 = Person()
del p1
