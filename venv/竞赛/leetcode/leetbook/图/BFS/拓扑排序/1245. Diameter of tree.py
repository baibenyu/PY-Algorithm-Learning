# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/10 9:18'

import time
from collections import defaultdict
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        adjVex = defaultdict(list)  # 邻接表
        for x, y in edges:  # 初始化邻接表，建图
            adjVex[x].append(y)
            adjVex[y].append(x)

        que = [0]
        visited = [False for _ in range(n + 1)]
        visited[0] = True
        cur = 0  # 全局变量，好记录第一次BFS最后一个点的ID,这个点实际上是当前树的最长直径的一个端点
        while que:
            cur_len = len(que)
            for _ in range(cur_len):
                cur = que.pop(0)
                for nxt in adjVex[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True  # 进队时visit和出队时visit都可以
                        que.append(nxt)
        visited = [False for _ in range(n + 1)]
        que = [cur]  # 第一次最后一个点，作为第二次BFS的起点
        visited[cur] = True
        level = -1  # 记好距离
        while que:
            cur_len = len(que)
            level += 1
            for _ in range(cur_len):
                cur = que.pop(0)
                for nxt in adjVex[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        que.append(nxt)
        return level


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
