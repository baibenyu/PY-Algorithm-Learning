# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/31 9:39'

import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])  # 扁平化
        return self.parent[x]

    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True


class Solution:
    # 方法一:Kruskal 算法--并查集判断是否同集合
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()
        uf = UnionFind(len(points))
        ans = 0
        for dis, x, y in edges:
            if uf.Union(x, y):
                ans += dis
        return ans

    # 方法二:Prim算法
    def minCostConnectPoints2(self, points: List[List[int]]) -> int:

        n = len(points)
        d = [float("inf")] * n  # 表示各个顶点与加入最小生成树的顶点之间的最小距离.
        vis = [False] * n  # 表示是否已经加入到了最小生成树里面
        d[0] = 0
        ans = 0
        for _ in range(n):
            # 寻找目前这轮的最小d
            M = float("inf")
            for i in range(n):
                if not vis[i] and d[i] < M:
                    node = i
                    M = d[i]
            vis[node] = True
            ans += M
            # 重点--实时更新与这个顶点相连接的顶点的d.
            for i in range(n):
                if not vis[i]:
                    d[i] = min(d[i], abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
