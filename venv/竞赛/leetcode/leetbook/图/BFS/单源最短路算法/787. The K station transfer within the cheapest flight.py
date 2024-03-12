# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/24 10:52'

import time
import collections
import heapq
from typing import List


class Solution:
    # 方法一:BFS
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if len(flights) == 0:
            return -1

        neibghbours = collections.defaultdict(list)
        for i, j, p in flights:
            neibghbours[i].append([j, p])

        # 检查起点和终点间是否有通路，没有则返回 -1
        visited = set()
        q = [src]
        while q:
            position = q.pop()
            visited.add(position)
            for nei, _ in neibghbours[position]:
                if nei not in visited:
                    q.append(nei)

        if dst not in visited:
            return -1

        # 用优先队列选择符合条件的最低价格,Dijkstra算法的优化
        pq = [[0, -1, src]]
        while pq:
            price, passed, position = heapq.heappop(pq)
            if position == dst:
                return price
            for nei_position, nei_price in neibghbours[position]:
                if passed + 1 <= k:
                    heapq.heappush(pq, [price + nei_price, passed + 1, nei_position])

        return -1

    # 方法二:SPFA算法--BF优化
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 9
        res = INF

        adjvex = collections.defaultdict(list)
        for x, y, cost in flights:
            adjvex[x].append((y, cost))

        dist = [[INF for _ in range(k + 2)] for _ in range(n)]
        minHeap = []

        dist[src][0] = 0
        heapq.heappush(minHeap, (0, src, 0))

        while minHeap:
            d, x, step = heapq.heappop(minHeap)
            if x == dst:
                res = d
                break
            if step == k + 1:
                continue
            for y, cost in adjvex[x]:
                dd = dist[x][step] + cost
                if dd < dist[y][step + 1]:  # 仅加入更新过的结点
                    dist[y][step + 1] = dd
                    heapq.heappush(minHeap, (dd, y, step + 1))

        return res if res != INF else -1

    # 方法三:动态规划--经典BF算法
    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)

        ans = min(f[t][dst] for t in range(1, k + 2))  # 最多k站,所以需要遍历所有1-k+2站所有花费中取最小
        return -1 if ans == float("inf") else ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
