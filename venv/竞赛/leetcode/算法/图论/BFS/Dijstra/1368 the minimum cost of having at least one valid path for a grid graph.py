# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/18 19:54'
import heapq
import time
from typing import List


class Solution:
    # 方法一:修改次数最少-->先将问题转为求最短路问题
    # Dijkstra算法+BFS,四方向移动,若与矩阵对应操作相同,视为边的权值为0,即无需修改,若不同,视为边的权值为1
    # 在最短路遍历过程中更新修改次数,即经历的边的总权值大小
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        BIG = int(1e9)
        dist = [0] + [BIG] * (m * n - 1)
        seen = set()
        q = [(0, 0, 0)]

        while len(q) > 0:
            cur_dis, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            cur_pos = x * n + y
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = nx * n + ny
                new_dis = dist[cur_pos] + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n and new_dis < dist[new_pos]:
                    dist[new_pos] = new_dis
                    heapq.heappush(q, (new_dis, nx, ny))

        return dist[m * n - 1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
