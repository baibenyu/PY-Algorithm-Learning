# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 15:56'

import time
from typing import List


class Solution:
    # 方法一:DP
    # dp表示每一行每一个位置花费的最小值
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]  # 开头和末尾只有一个可选
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
