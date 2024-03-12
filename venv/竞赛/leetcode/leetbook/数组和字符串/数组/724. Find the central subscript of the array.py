# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/7 8:37'

import time
from typing import List


class Solution:
    # 方法一:前缀和
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = list()
        prefix.append(0)
        for i in range(1, len(nums)+1):
            prefix.append(nums[i-1] + prefix[i - 1])
        for j in range(len(nums)):
            if prefix[j] == prefix[-1]-prefix[j+1]:
                return j
        return -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
