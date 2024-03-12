# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 7:59'

import time
from typing import List


class Solution:
    # 方法一:DP--01背包
    # 这题可以将概率视为硬币的价值,背包容量为t,每个朝上的硬币的体积为1
    # dp[i][j]表示前i-1个硬币有j-1个朝上的硬币的概率
    def probabilityOfHeads(self, ps: List[float], t: int) -> float:
        n = len(ps)
        if n < t:
            return 0
        dp = [[0] * (t + 1) for _ in range(n + 1)]

        dp[0][0] = 1
        # 初始化
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] * (1 - ps[i - 1])  # 全都朝下的概率
        # 转移
        for i in range(1, n + 1):
            x = ps[i - 1]  # 正面概率
            for j in range(1, min(t + 1, i + 1)):
                # 前i-1个硬币有j-1个朝上的硬币的概率 = 前i-2个硬币有j-2个朝上的硬币的概率*当前硬币为正面的概率+前i-2个硬币有j-1个朝上的硬币的概率*当前硬币为反面的概率
                dp[i][j] = dp[i - 1][j - 1] * x + dp[i - 1][j] * (1 - x)
        return dp[n][t]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
