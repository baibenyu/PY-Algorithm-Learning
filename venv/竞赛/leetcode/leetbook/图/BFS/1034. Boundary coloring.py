# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/7 9:12'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:BFS--在遍历连通分量过程中多加一步判断是否是边界
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        originalColor = grid[row][col]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque([(row, col)])
        visited[row][col] = True
        while q:
            x, y = q.popleft()
            isBorder = False
            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                    isBorder = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            if isBorder:
                borders.append((x, y))
        for x, y in borders:
            grid[x][y] = color
        return grid

    # 方法二:DFS
    def colorBorder2(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        originalColor = grid[row][col]
        visited[row][col] = True
        self.dfs(grid, row, col, visited, borders, originalColor)
        for x, y in borders:
            grid[x][y] = color
        return grid

    def dfs(self, grid, x, y, visited, borders, originalColor):
        isBorder = False
        m, n = len(grid), len(grid[0])
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                isBorder = True
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                self.dfs(grid, nx, ny, visited, borders, originalColor)
        if isBorder:
            borders.append((x, y))


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
