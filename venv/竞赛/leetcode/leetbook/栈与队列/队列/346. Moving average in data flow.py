# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 17:40'

import time
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.cur = 0

    def next(self, val: int) -> float:
        if self.size > 0:
            self.size -= 1
            self.q.append(val)
            self.cur += val
            return self.cur / len(self.q)
        else:
            self.cur -= self.q.popleft()
            self.q.append(val)
            self.cur += val
            return self.cur / len(self.q)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
