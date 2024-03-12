# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/6 9:34'
import collections
from typing import List


class Solution:
    # 方法一:BFS+拓扑排序
    # 拓扑排序是一种对依赖关系进行排序的算法,依赖少的在前面
    # 对应图中的有向无环图
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])  # 存储依赖关系
            indeg[info[0]] += 1  # 存储入度

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:  # 直至无入度为0的节点
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1  # 去除当前节点对后续节点的影响,即减少后续节点的入度
                if indeg[v] == 0:  # 若入度为0则入队
                    q.append(v)

        return visited == numCourses  # 若入度能为0的节点数与课程数相等说明,每一门课都能学,否则存在环或选修课程数不够
