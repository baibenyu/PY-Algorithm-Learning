# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 20:39'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:BFS
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))  # 从每一个点出发
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0

        while q:
            u, mask, dist = q.popleft()  # mask用二进制位上的1标记经过了哪些结点
            if mask == (1 << n) - 1:
                ans = dist
                break
            # 搜索相邻的节点
            for v in graph[u]:
                # 将 mask 的第 v 位置为 1
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
