# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/29 9:18'

import time
from typing import List


class Solution(object):
    # 方法一:贪心--将每个偶数下标上的匹配对象交换到对应位置
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)
        res = 0
        for i in range(0, N - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                continue
            for j in range(i + 1, N):
                if row[i] == row[j] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
            res += 1
        return res


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

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


class Solution2:
    # 方法二:并查集--如果不归属于同一组需要交换,归属于同一组则无需交换
    # 至少交换的次数 = 所有情侣的对数 - 并查集里连通分量的个数
    def minSwapsCouples(self, row: List[int]) -> int:
        uf = UnionFind(len(row))
        for i in range(0, len(row), 2):
            uf.Union(row[i] // 2, row[i + 1] // 2)  # 构造连通片

        return len(row) - uf.part


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
