# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 15:18'

import time


class Solution(object):
    # 方法一:动态规划
    # 实际就是分类讨论--1.考虑偷开头的屋子不偷末尾 2. 考虑偷末尾的屋子不偷开头
    def rob(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        return max(self.rob1(nums[0:N - 1]), self.rob1(nums[1:N]))

    def rob2(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
