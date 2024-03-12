# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 20:27'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:BFS
    # 对于每一个都在g1中,直接遍历判断即可
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def bfs(sx: int, sy: int) -> int:
            q = deque([(sx, sy)])
            grid2[sx][sy] = 0
            # 判断岛屿包含的每一个格子是否都在 grid1 中出现了
            check = (grid1[sx][sy] == 1)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                        q.append((nx, ny))
                        grid2[nx][ny] = 0
                        if grid1[nx][ny] != 1:
                            check = False

            return int(check)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += bfs(i, j)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
