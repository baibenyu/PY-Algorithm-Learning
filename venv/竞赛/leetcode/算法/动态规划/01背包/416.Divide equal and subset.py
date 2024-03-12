# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/1 19:25'
from typing import List


class Solution:
    # 方法一:动态规划--01背包
    # dp[i][j]表示状态在0-i的下标内取数字,能达成j的是否存在
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):  # 遍历物品下标
            num = nums[i]
            for j in range(1, target + 1):  # 遍历背包容量
                if j >= num:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]
