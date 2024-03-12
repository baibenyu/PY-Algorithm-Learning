# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/21 10:38'

import time
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:  # 仅含0的情况
            return 0
        if 0 not in nums:  # 仅含1的情况
            return len(nums) - 1

        # 情况三:结果的窗口必然是由1和0共同构成的
        n = len(nums)
        res = 0
        cnt0 = 0
        L = 0
        for R in range(n):  # 滑动窗口 进R
            if nums[R] == 0:
                cnt0 += 1

            while cnt0 > 1:  # 弹L
                if nums[L] == 0:
                    cnt0 -= 1
                L += 1

            res = max(res, R - L + 1)  # 更新res
        return res - 1  # 减去0


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
