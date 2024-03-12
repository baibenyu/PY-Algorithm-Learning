# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 20:26'

import time
from typing import List


class Solution:
    # 方法一:BFS
    # 实际从0点出发,遍历相连的点,若是入度则说明可达,无需变动该路线,若是出度则需要倒转
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge = [[] for _ in range(n)]
        for p, c in connections:
            edge[p].append((c, 1))
            edge[c].append((p, 0))
        quee = [0]
        vist = [False] * n
        vist[0] = True
        ans = 0
        while quee:
            i = quee.pop(0)
            for n, c in edge[i]:
                if not vist[n]:
                    vist[n] = True
                    ans += c
                    quee.append(n)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
