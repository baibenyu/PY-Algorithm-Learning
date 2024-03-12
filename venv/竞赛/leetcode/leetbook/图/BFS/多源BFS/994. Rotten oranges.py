# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/29 21:51'
import collections
import time
from typing import List


class Solution:
    # 方法一:BFS+超级源头
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        flag = 0
        q = collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if grid[i][j] == 2:
                        q.append((i, j))
                    else:
                        flag = 1

        if not flag:
            return 0

        isvis = {each for each in q}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minute = -1
        while q:
            for i in range(len(q)):
                dx, dy = q.popleft()
                for each in directions:
                    x = dx + each[0]
                    y = dy + each[1]
                    if 0 <= x < m and 0 <= y < n and (x, y) not in isvis:
                        isvis.add((x, y))
                        if grid[x][y] == 1:
                            q.append((x, y))
                        grid[x][y] = 2
            minute += 1

        for each in grid:
            if 1 in each:
                return -1
        else:
            return minute

    # 同理,将时间也入队
    def orangesRotting2(self, grid: List[List[int]]) -> int:
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        # add the rotten orange to the queue
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        # bfs
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))
        # if there are still fresh oranges, return -1
        for row in grid:
            if 1 in row:
                return -1

        return time


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
