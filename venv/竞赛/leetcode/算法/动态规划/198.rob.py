# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 14:51'

import time
from typing import List


class Solution:
    # 方法一:动态规划
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return nums[0]
        dp = [[0, 1] for i in range(length)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        dp[1][0] = max(dp[0][0], dp[0][1])
        dp[1][1] = dp[0][0] + nums[1]
        for i in range(2, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + nums[i]
        return max(dp[length - 1][0], dp[length - 1][1])

    # DP优化
    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])  # 只能间隔着偷,或者不偷

        return dp[size - 1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
