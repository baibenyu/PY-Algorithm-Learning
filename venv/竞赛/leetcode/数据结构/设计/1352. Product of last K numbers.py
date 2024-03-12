# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 19:25'

import time
class ProductOfNumbers:

    def __init__(self):
        self.p = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.p = [1]
        else:
            self.p.append(self.p[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.p): return 0
        return self.p[-1] // self.p[-k-1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
