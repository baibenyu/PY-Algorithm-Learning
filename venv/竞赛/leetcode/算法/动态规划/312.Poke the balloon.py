# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/2 9:55'
from typing import List


class Solution:
    # 方法一:动态规划
    # dp表示在前后加上1方便处理边界后的(i,j)开区间内,戳气球能得到的最大硬币数,k用遍历于i,j区间内以k为最后一个被戳破的气球的情况,即遍历所有戳法选出最大的
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.insert(len(nums), 1)
        length = len(nums)
        dp = [[0] * length for i in range(length)]

        for i in range(length - 3, -1, -1):
            for j in range(i + 2, length):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][length - 1]