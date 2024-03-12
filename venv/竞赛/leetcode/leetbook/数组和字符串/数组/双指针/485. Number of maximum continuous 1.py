# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 10:19'

import time
from typing import List


class Solution:
    # 方法一:双指针
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right, ans = 0, 0, 0
        while left < len(nums):
            while left < len(nums) and nums[left] != 1:
                left += 1
            while left + right < len(nums) and nums[left + right] == 1:
                right += 1
            left = left + right
            ans = max(ans, right)
            right = 0
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
