# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/4 19:29'

import time
from random import random
from typing import List


class Solution:
    # 方法一:模拟
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = [0] * len(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
