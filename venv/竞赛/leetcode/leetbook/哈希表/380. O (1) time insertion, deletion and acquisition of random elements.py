# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/14 9:25'

import time
from random import random


class RandomizedSet:

    def __init__(self):
        self.dict1 = set()
        self.dict2 = list()

    def insert(self, val: int) -> bool:
        if val not in self.dict1:
            self.dict1.add(val)
            self.dict2.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict1:
            self.dict1.remove(val)
            self.dict2.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.dict2)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
