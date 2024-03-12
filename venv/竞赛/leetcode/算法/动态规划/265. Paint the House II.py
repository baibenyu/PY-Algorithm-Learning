# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/12 15:51'

import time
from typing import List


class Solution:
    # 方法一:DP--同256
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        for j in range(k):  # 初始化
            dp[0][j] = costs[0][j]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])  # 当前颜色+其它颜色中花费较小的
        return min(dp[n - 1])


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
