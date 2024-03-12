# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 8:47'

import time
from typing import List


class UF:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        if x == y:
            return
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.p[rx] = ry


class Solution:
    # 方法一:并查集
    # 每插入一个陆地,都与上下左右合并,求连通分量个数
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        seen = set()
        uf = UF(m * n)
        count = 0
        res = []
        for pos in positions:
            x, y = pos
            if (x, y) in seen:
                res.append(count)
                continue
            idx = x * n + y
            seen.add((x, y))
            count += 1
            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if (nx, ny) not in seen:
                    continue
                idx2 = nx * n + ny
                rx = uf.find(idx)
                ry = uf.find(idx2)
                if rx != ry:
                    uf.union(idx, idx2)
                    count -= 1
            res.append(count)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
