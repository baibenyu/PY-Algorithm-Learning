# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/29 10:40'

import time
from typing import List


class Union:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True


class Solution:
    # 方法一:并查集--将斜杠构成的可能情况分解为四个不可再分的三角形,这些三角形就是图结构中的结点,然后求连通分量
    def regionsBySlashes(self, grid: List[str]) -> int:
        # m 每行方框数量 方框内部有四个三角形！
        m = len(grid)
        n = (m ** 2) * 4
        uf = Union(n)
        # 初始联系初始化！
        k = 0
        for i in range(m):
            # if i != len(grid)-1:
            #     i1
            for j in range(len(grid[i])):
                # 方框外部连接！不受 / 和 \ 影响
                if j != len(grid) - 1:
                    uf.unite(k * 4 + 2, (k + 1) * 4)
                if i != len(grid) - 1:
                    uf.unite(k * 4 + 3, (k + m) * 4 + 1)

                # 方框内部
                if grid[i][j] == "/":
                    uf.unite(k * 4, k * 4 + 1)
                    uf.unite(k * 4 + 2, k * 4 + 3)
                elif grid[i][j] == " ":
                    uf.unite(k * 4, k * 4 + 1)
                    uf.unite(k * 4 + 1, k * 4 + 2)
                    uf.unite(k * 4 + 2, k * 4 + 3)
                    uf.unite(k * 4 + 3, k * 4)
                elif grid[i][j] == "\\":
                    # 仅查询\字符
                    uf.unite(k * 4 + 1, k * 4 + 2)
                    uf.unite(k * 4 + 3, k * 4)
                k += 1

        return uf.setCount


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
