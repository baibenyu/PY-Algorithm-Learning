# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 20:11'

import time
from typing import List


class Solution:
    # 方法一:BFS
    # 曼哈顿距离实际上相当于要经过的格子数
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)

        queue = []
        # 将所有的陆地格子加入队列,将所有周围一步的海洋访问一遍,并加入这些海洋之外的相邻海洋,循环直至所有海洋都被访问,最终遍历的次数即距离
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
        # 如果我们的地图上只有陆地或者海洋，请返回 -1。
        if len(queue) == 0 or len(queue) == N * N:
            return -1

        distance = -1
        while len(queue) > 0:
            distance += 1
            # 这里一口气取出 n 个结点，以实现层序遍历
            n = len(queue)
            for i in range(n):
                r, c = queue.pop(0)
                # 遍历上边单元格
                if r - 1 >= 0 and grid[r - 1][c] == 0:
                    grid[r - 1][c] = 2
                    queue.append((r - 1, c))
                # 遍历下边单元格
                if r + 1 < N and grid[r + 1][c] == 0:
                    grid[r + 1][c] = 2
                    queue.append((r + 1, c))
                # 遍历左边单元格
                if c - 1 >= 0 and grid[r][c - 1] == 0:
                    grid[r][c - 1] = 2
                    queue.append((r, c - 1))
                # 遍历右边单元格
                if c + 1 < N and grid[r][c + 1] == 0:
                    grid[r][c + 1] = 2
                    queue.append((r, c + 1))

        return distance


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
