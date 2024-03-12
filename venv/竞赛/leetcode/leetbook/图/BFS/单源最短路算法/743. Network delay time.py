# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/1 8:19'

import time
from typing import List


class Solution:
    # 方法一:Dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float('inf') for _ in range(n)] for _ in range(n)]  # 边的初始化
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float('inf') for _ in range(n)]  # 距离初始化
        dist[k - 1] = 0
        used = [False for _ in range(n)]
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):  # 遍历未访问的元素
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):  # 更新最短距离
                if not used[y]:
                    dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
