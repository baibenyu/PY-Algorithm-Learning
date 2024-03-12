# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/19 10:10'

import time
from typing import List


class Solution:
    # 方法一:滑动窗口
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        start = 0

        for i in range(n):
            if i > 0 and nums[i] <= nums[i - 1]:
                start = i
            ans = max(ans, i - start + 1)

        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
