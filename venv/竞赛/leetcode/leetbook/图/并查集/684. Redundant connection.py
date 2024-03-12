# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/29 8:58'

import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

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
    # 方法一:并查集
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.Union(edge[0], edge[1]):
                return edge


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
