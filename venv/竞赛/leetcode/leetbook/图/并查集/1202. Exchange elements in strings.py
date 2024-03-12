# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/30 9:26'

import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.count = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]
        self.parts = [[x] for x in range(n)]

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
        self.parts[root_y].extend(self.parts[root_x])
        self.parts[root_x] = None
        self.count -= 1
        return True


class Solution:
    # 方法一:并查集--因为可以任意次交换,即可交换的位置都是连通的,若要找到最小字典序,即保证每个独立的连通分量都也得是最小字典序排列
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        ans = [None for _ in range(len(s))]
        for each in pairs:
            uf.Union(each[0], each[1])
        for part in uf.parts:
            if part:
                temp = []
                for a in part:
                    temp.append(s[a])
                temp.sort()
                part.sort()
                for i in range(len(part)):
                    ans[part[i]] = temp[i]
        return "".join(ans)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
