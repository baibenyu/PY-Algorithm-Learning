# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/18 8:37'

import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.size = [1 for x in range(n)]
        self.part = n

    # ----------- 扁平化
    def Find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    # ---------- size策略
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

    def connected(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)

    def get_part_size(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]


class Solution:
    # 方法一:类kruskal算法--并查集+BFS,至少为
    # 思路:将所有边的权值按从大到小排序,依次连接结点,直至题目要求的两个点连通为止
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        Row, Col = len(A), len(A[0])
        n = Row * Col
        UF = UnionFind(n)
        a = []
        for r in range(Row):
            for c in range(Col):
                a.append((A[r][c], r, c))
        a.sort()
        # ----------------- 并查集--check连通性
        res = min(A[0][0], A[Row - 1][Col - 1])  # 因为在运算过程中，这两个点的val没有与res比较
        visited = set()
        visited.add(0)
        visited.add(n - 1)
        while not UF.connected(0, n - 1):
            cost, r, c = a.pop(-1)
            ID = r * Col + c
            res = min(res, cost)
            visited.add(ID)
            # ----------- 4个方向 在visited里，就可以Union,因为前面建立的权值并不保证两个点是相邻的,只有碰到相邻结点才能连通
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < Row and 0 <= nc < Col:
                    nxt_ID = nr * Col + nc
                    if nxt_ID in visited:
                        UF.Union(ID, nxt_ID)
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
