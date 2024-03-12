# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 17:00'

import time
from typing import List


class Solution:
    # 方法一:DP
    # dp[[i][j]表示到达(i,j)点所需的最少起始点,最大路径和不等于最少起始点,在路上有一个遇到怪物和治疗先后的问题,必须先解决怪物才能得到治疗
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float("inf") for _ in (m + 1)] for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        # 逆序保证无后效性,
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])  # 左右最小需要的起始点
                dp[i][j] = max(minn - dungeon[i][j], 1)  # 减去当前给予的起始点

        return dp[0][0]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
