# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/4 10:11'
import collections
import time
from typing import List


class Solution:
    # 方法一:DFS
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(x, y):
            for i in range(n):
                if isConnected[x][i] == 1:
                    isConnected[x][i] = 0
                    isConnected[i][x] = 0
                    dfs(i, 0)

        count = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    count += 1
                    dfs(i, j)

        return count

    # 方法二:BFS
    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1

        return circles

    # 方法三:并查集
    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        provinces = len(isConnected)
        parent = list(range(provinces))

        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(provinces))
        return circles


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
