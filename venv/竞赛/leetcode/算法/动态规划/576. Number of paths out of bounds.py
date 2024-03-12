# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 19:30'

import time


class Solution:
    # 方法一:DP
    # dp[i][j][k]表示移动i次到达(j,k)坐标点的次数
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        outCounts = 0
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % MOD
                            else:  # 出界时加到结果上
                                outCounts = (outCounts + dp[i][j][k]) % MOD

        return outCounts


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
