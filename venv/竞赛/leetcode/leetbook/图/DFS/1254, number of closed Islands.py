# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 10:25'

import time
from typing import List


class Solution:
    # 方法一:DFS
    # 与边界相连的土地不可能是封闭土地,所以先遍历边界将0置为1,再对整体DFS
    # 注意只要与边界相连就得置为1,而不是只将边界置为1,岛屿是一个整体
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if grid[x][y] == 1:
                return
            grid[x][y] = 1
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < m and 0 <= my < n:
                    dfs(mx, my)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    ans += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
