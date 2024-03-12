# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/30 9:56'

import time
from typing import List


class UF:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0
        # 初始化 parent，size 和 cnt
        for i in range(M):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        leader_p = self.find(p)
        leader_q = self.find(q)
        self.parent[leader_p] = leader_q
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    # 方法一:并查集--判断所有石子两两相连,而不是判断相邻石子
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        return n - uf.cnt


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
