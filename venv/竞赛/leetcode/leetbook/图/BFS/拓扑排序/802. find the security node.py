# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 16:33'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:DFS+三色标记法
    # 本题实际上就在找不属于环的结点
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n

        def safe(x: int) -> bool:
            if color[x] > 0:  # 如果已经搜索过,返回结果
                return color[x] == 2  # 如果搜索过但不确定状态,现在又碰到说明有环,返回False
            color[x] = 1  # 否则标记为已访问,但尚不确定结果
            for y in graph[x]:  # 遍历下一节点,对于所有下一节点,若找到环,则返回False
                if not safe(y):
                    return False
            color[x] = 2  # 无环说明安全
            return True

        return [i for i in range(n) if safe(i)]

    # 方法二:逆图后进行拓扑排序
    def eventualSafeNodes2(self, graph: List[List[int]]) -> List[int]:
        rg = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:  # 逆序存储图的入度和出度,生成逆图
                rg[y].append(x)
        in_deg = [len(ys) for ys in graph]  # 将原图的出度存储为逆图的入度

        q = deque([i for i, d in enumerate(in_deg) if d == 0])  # 存储入度可为0的节点
        while q:
            for x in rg[q.popleft()]:
                in_deg[x] -= 1
                if in_deg[x] == 0:
                    q.append(x)

        return [i for i, d in enumerate(in_deg) if d == 0]  # 若入度为0说明安全,小于0说明有环


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
