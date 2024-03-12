# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 15:19'

import time


class MRUQueue:

    def __init__(self, n: int):
        self.tmp = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        res = self.tmp[k - 1]
        self.tmp[k - 1:] = self.tmp[k:]
        self.tmp.append(res)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
