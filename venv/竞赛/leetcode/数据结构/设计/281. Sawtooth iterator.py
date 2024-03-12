# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 10:31'

import time
from typing import List


class ZigzagIterator:
    # 方法一:模拟
    def __init__(self, v1: List[int], v2: List[int]):
        self.all = [v1, v2]
        self.arr = [[0, len(v1)], [0, len(v2)]]
        self.sum_up = len(v1) + len(v2)
        self.cur = 0

    def next(self) -> int:
        if self.hasNext():
            while self.arr[self.cur][0] >= self.arr[self.cur][1]:
                self.cur = (self.cur + 1) % len(self.all)
            temp = self.all[self.cur][self.arr[self.cur][0]]
            self.arr[self.cur][0] += 1
            self.cur = (self.cur + 1) % len(self.all)
            self.sum_up -= 1
            return temp
        else:
            return False

    def hasNext(self) -> bool:
        if self.sum_up > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
