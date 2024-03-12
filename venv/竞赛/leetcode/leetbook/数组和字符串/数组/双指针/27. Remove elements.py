# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 10:03'

import time
from typing import List


class Solution:
    # 方法一:双指针
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
