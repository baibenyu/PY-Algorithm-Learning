# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 9:38'

import time

from jinja2.nodes import List


class Solution:
    # 方法一:BFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        import collections
        maxarea = 0
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        for r in range(nr):
            for c in range(nc):
                num_area = 0
                if grid[r][c] == 1:
                    num_area += 1
                    grid[r][c] = 0
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:
                                num_area += 1
                                neighbors.append((x, y))
                                grid[x][y] = 0
                    maxarea = max(maxarea, num_area)
        return maxarea

    # 方法二:DFS
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
