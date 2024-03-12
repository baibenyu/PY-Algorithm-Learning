# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 16:47'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:DFS--经典回溯
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)

        def dfs(cur, temp):
            nonlocal ans
            if cur == n - 1:
                ans.append(temp.copy())
                return
            else:
                for each in graph[cur]:
                    temp.append(each)
                    dfs(each, temp)
                    temp.pop()

        dfs(0, [0])
        return ans

    # 方法二:BFS
    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])
        ans = []
        while q:
            path = q.popleft()
            if path[-1] == n - 1:
                ans.append(path)
                continue
            for nxt in graph[path[-1]]:
                q.append(path + [nxt])
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
