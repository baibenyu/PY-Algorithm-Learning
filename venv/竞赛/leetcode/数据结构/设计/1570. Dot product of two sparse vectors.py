# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/25 15:29'

import time
from typing import List


class SparseVector:
    # 方法一:模拟
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(len(self.nums)):  # 无脑计算
            res += self.nums[i] * vec.nums[i]
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
