# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/1 12:07'
from typing import List


class Solution:
    # 方法一:动态规划
    # 区别于最大子数组和,增加了一个状态,为什么这么做呢?因为乘积的最大值即可能是由两个同号的数字相乘得到,而不仅是正数,局部最大值不等于全局最大值
    # dp[i][0]表示前i个数的最大乘积,dp[i][1]表示前i个数的最小乘积
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        length = len(nums)
        dp = [[float("-inf"), float("inf")] for i in range(length)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
            res = max(res, dp[i][0])
        return res
