# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/24 16:17'

import time
from typing import List


class Solution:
    # 方法一:DP
    #  dp[i][j][k]表示位于矩阵第i行,第j列的连续1的k种可能的数目
    def longestLine(self, M: List[List[int]]) -> int:
        # 左上到右下为主对角线(major diagnoal)，右上到左下为辅对角线(minor or anti diagnoal)
        if not M or not M[0]:
            return 0

        res = 0
        m = len(M)
        n = len(M[0])
        dp = [[[0] * 4 for i in range(0, n + 2)] for j in range(0, m + 1)]
        for i in range(1, m + 1):  # 因为遍历顺序从左到右,从上往下
            for j in range(1, n + 1):
                if M[i - 1][j - 1] == 0:
                    continue

                dp[i][j][0] = dp[i][j - 1][0] + 1  # row dir 向左
                dp[i][j][1] = dp[i - 1][j][1] + 1  # col dir 向右
                dp[i][j][2] = dp[i - 1][j - 1][2] + 1  # major dir 向左上
                dp[i][j][3] = dp[i - 1][j + 1][3] + 1  # minor dir (anti dir) 向右上

                for k in range(0, 4):
                    res = max(res, dp[i][j][k])

        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
