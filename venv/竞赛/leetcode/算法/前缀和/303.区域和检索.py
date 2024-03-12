# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/1 8:24'

import time
from typing import List


class NumArray:
    # 方法一:前缀和
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for i in range(1, len(nums) + 1):
            self.prefix.append(self.prefix[i - 1] + nums[i - 1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
