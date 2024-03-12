# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 18:45'

import time
from typing import List


class Solution:
    # 方法一:建立邻接表,统计入度和出度的和,枚举取最大
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for edge in roads:
            if edge[0] < edge[1]:
                start, end = edge[0], edge[1]
            else:
                start, end = edge[1], edge[0]
            g[start].append((start, end))
            g[end].append((start, end))
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, len(set(g[i]) | set(g[j])))
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
