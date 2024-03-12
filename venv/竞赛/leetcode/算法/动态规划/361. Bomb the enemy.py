# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 19:46'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        Row = len(grid)
        if Row == 0:
            return 0
        Col = len(grid[0])
        # 思路： 从4个方向，向中心聚拢
        dp = [[0 for _ in range(Col)] for _ in range(Row)]

        # 先每行
        for r in range(Row):
            # 从左至右
            cnt = 0
            for c in range(Col):
                if grid[r][c] == 'W':
                    cnt = 0
                elif grid[r][c] == 'E':
                    cnt += 1
                dp[r][c] += cnt
            # 从右至左
            cnt = 0
            for c in range(Col - 1, -1, -1):
                if grid[r][c] == 'W':
                    cnt = 0
                elif grid[r][c] == 'E':
                    cnt += 1
                dp[r][c] += cnt
        # 再每列
        for c in range(Col):
            # 从上至下
            cnt = 0
            for r in range(Row):
                if grid[r][c] == 'W':
                    cnt = 0
                elif grid[r][c] == 'E':
                    cnt += 1
                dp[r][c] += cnt
            # 从下往上
            cnt = 0
            for r in range(Row - 1, -1, -1):
                if grid[r][c] == 'W':
                    cnt = 0
                elif grid[r][c] == 'E':
                    cnt += 1
                dp[r][c] += cnt
        res = 0
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == '0':  # 只有0的地方，才能放炸弹
                    res = max(res, dp[r][c])
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
