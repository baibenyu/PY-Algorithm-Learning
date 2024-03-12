# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 20:06'
from typing import List


class Solution:
    # 方法一:动态规划,多状态动态规划
    # 各天的状态是当天操作完以后的状态
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for i in range(n)]  # dp的初始化

        dp[0][0] = 0  # 第0天不持股自然就为0了
        dp[0][1] = -prices[0]  # 第0天持股，那么价格就是-prices[0]了
        # 第1天不持股，要么第0天就不持股，要么就是第0天持股，然后第1天卖出
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        # 第一天持股，要么就是第0天就持股了，要么就是第0天不持股第1天持股
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])  # i-2是因为冷冻期对买入限制,如果i-1的话,即昨天,昨天不持有股票可
            # 能是因为昨天刚卖,这样会导致今天冷冻,不能买入,等式不成立,所以用i-2来表示前天,前天卖昨天冷冻今天解冻,等式成立
        return dp[-1][0]

    # 优化
    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])
