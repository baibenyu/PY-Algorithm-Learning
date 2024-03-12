# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 21:05'

import time
from typing import List


class Solution:
    # 方法一:动态规划,总共n+1级台阶
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float("inf") for _ in range(len(cost) + 1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[len(cost)]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
