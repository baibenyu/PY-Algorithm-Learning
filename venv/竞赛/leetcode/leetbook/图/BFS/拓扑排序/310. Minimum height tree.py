# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/31 11:02'

import time
from typing import List


class Solution:
    # 方法一:拓扑排序
    # 要想树的高度尽可能低,那么根结点的之外的结点应该尽量分配平均,即应该尽量向平衡树靠,即在有限的高度内塞下尽可能多的结点
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]  # 从度为1(叶子结点)的结点开始遍历
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1  # 删除影响
                    if deg[y] == 1:
                        q.append(y)
        return q


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
