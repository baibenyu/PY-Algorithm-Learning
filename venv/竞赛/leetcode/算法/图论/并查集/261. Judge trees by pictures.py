# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/24 17:32'

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
            self.parent[x] = self.Find(self.parent[x])  ##扁平化
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

    def in_the_same_part(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)

    def get_part_size(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = UnionFind(n)
        for x, y in edges:
            if not UF.Union(x, y):  # 失败了，说明已经在一个连通域中了。再连接就是环了
                return False
        return UF.part == 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
