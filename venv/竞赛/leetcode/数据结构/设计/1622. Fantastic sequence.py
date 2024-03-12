# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 15:35'

import time

mod = 10 ** 9 + 7


class Fancy:

    def __init__(self):
        self.ls = []
        self.add = [0]  # 偏移前缀和
        self.mult = [1]  # 偏移前缀积

    def append(self, val: int) -> None:
        self.ls.append(val)
        self.add.append(self.add[-1])
        self.mult.append(self.mult[-1])

    def addAll(self, inc: int) -> None:
        self.add[-1] += inc

    def multAll(self, m: int) -> None:
        self.mult[-1] *= m
        self.mult[-1] %= mod
        self.add[-1] *= m
        self.add[-1] %= mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.ls):
            return -1
        inv = pow(self.mult[idx], mod - 2, mod)  # 数论相关,群论,不知道!!!
        return ((self.ls[idx] - self.add[idx]) * self.mult[-1] * inv + self.add[-1]) % mod


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
