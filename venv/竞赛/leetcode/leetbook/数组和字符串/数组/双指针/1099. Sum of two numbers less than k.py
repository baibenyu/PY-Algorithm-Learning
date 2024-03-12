# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 9:22'

import time
from typing import List


class Solution:
    # 方法一:排序+双指针
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = -0x3f3f3f3f
        L, R = 0, n - 1
        while L < R:
            if nums[L] + nums[R] >= k:
                R -= 1
            else:
                res = max(res, nums[L] + nums[R])
                L += 1
        return res if res != -0x3f3f3f3f else -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
