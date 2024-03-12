# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 19:59'

import time
from typing import List


class Solution:
    # 方法一:DFS
    # 将与边界相连的1置为0,然后再统计1的个数
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if grid[x][y] == 0:
                return
            grid[x][y] = 0
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < m and 0 <= my < n:
                    dfs(mx, my)

        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][n - 1] == 1:
                dfs(i, n - 1)
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[m - 1][j] == 1:
                dfs(m - 1, j)
        ans = 0
        for i in range(m):
            ans += grid[i].count(1)
        return ans


# 方法二:并查集,在合并的时候标记是否处于边界
class UnionFind:
    def __init__(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        self.parent = [0] * (m * n)
        self.rank = [0] * (m * n)
        self.onEdge = [False] * (m * n)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    idx = i * n + j
                    self.parent[idx] = idx
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        self.onEdge[idx] = True

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.onEdge[x] |= self.onEdge[y]
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.onEdge[y] |= self.onEdge[x]
        else:
            self.parent[y] = x
            self.onEdge[x] |= self.onEdge[y]
            self.rank[x] += 1


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        uf = UnionFind(grid)
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    idx = i * n + j
                    if j + 1 < n and grid[i][j + 1]:
                        uf.merge(idx, idx + 1)
                    if i + 1 < m and grid[i + 1][j]:
                        uf.merge(idx, idx + n)
        return sum(
            grid[i][j] and not uf.onEdge[uf.find(i * n + j)] for i in range(1, m - 1) for j in range(1, n - 1))


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
