# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/28 14:00'
from typing import List


class Solution:
    # 方法一:动态规划
    # dp[i]表示拥有i元所需最少硬币数
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        length = len(coins)
        coins.sort()  # 方便剪枝
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(length):  # i只可能通过不同面额的硬币来组合得到
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)  # 遍历length-1种不同金额达成i中,选所需硬币最少的那一个
                else:  # 当硬币面额大于所拥有的钱时退出循环
                    break
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
