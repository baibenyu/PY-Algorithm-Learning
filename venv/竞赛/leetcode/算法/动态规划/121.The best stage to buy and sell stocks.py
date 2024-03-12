# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 10:30'

import time
from typing import List


class Solution:
    # 方法一:动态规划,二维数组
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for i in range(n)]  # dp的初始化

        dp[0][0] = 0  # 第0天不持股自然就为0了
        dp[0][1] = -prices[0]  # 第0天持股，那么价格就是-prices[0]了

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])  # 只能买入和卖出一次,否则应该加上上面的dp
        return dp[-1][0]

    # 动态规划优化
    # 第i天的最大收益只需要知道前i天的最低点就可以算出来了。而第i天以前（包括第i天）的最低点和i-1天的最低点有关
    # dp[i] = min(dp[i-1],prices[i])
    # dp求的是前i天的最低购入点,在过程中维护一个最大利润
    def maxProfit2(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
