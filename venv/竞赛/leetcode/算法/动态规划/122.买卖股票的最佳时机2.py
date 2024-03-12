# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 9:03'

import time
from typing import List


class Solution:
    # 方法一:dp
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for i in range(n)]  # dp的初始化

        dp[0][0] = 0  # 第0天不持股自然就为0了
        dp[0][1] = -prices[0]  # 第0天持股，那么价格就是-prices[0]了

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]



if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
