# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/30 8:30'
import heapq
import time
from typing import List


class Solution:
    # 方法一:二分+遍历尝试--二分可能的时间范围,用DFS查找是否存在路径可以到达右下角
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(t, x, y, visited):
            if x == y == n - 1:
                return True
            visited[x][y] = True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] <= t:
                    if dfs(t, nx, ny, visited):
                        return True
            return False

        left = max(grid[0][0], grid[-1][-1])
        right = n * n - 1
        while left <= right:
            mid = (left + right) // 2
            visited = [[False] * n for _ in range(n)]
            if dfs(mid, 0, 0, visited):
                right = mid - 1
            else:
                left = mid + 1
        return left

    # 方法二:堆+BFS
    def swimInWater2(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        while heap:
            height, x, y = heapq.heappop(heap)
            res = max(res, height)
            if x == n - 1 and y == n - 1:
                return res

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    heapq.heappush(heap, (grid[new_x][new_y], new_x, new_y))

        return -1


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution1:
    # 方法三:并查集--判断连通所需最短时间,可以随时间一个个连通
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        n = len(grid)

        # 因为需要从小到大考虑时刻 t，从平台高度 t 出发判断是否能与相邻的方块连通
        # 所以这里需要存储每个平台高度对应的位置
        idx = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                idx[grid[i][j]] = (i, j)

        # print(idx)
        uf = UnionFind(n * n)
        for t in range(n * n):
            # 对高度为 t 的平台进行判断是否能与相邻四个方位的平台连通
            x, y = idx[t]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <= t:
                    # 尝试合并相邻的平台
                    uf.union(x * n + y, nx * n + ny)

            # 检查左下角与右下角是否连通，
            # 若能连通，此时的 t 即是答案
            if uf.connected(0, n * n - 1):
                return t

        return -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
