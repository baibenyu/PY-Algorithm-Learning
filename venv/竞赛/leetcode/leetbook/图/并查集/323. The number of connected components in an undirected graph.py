# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 8:59'

import time
from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
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

    def in_the_same_part(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)

    def get_part_size(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]


class Solution:
    # 方法一:并查集--经典用法求连通分量
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = UnionFind(n)
        for x, y in edges:
            UF.Union(x, y)
        return UF.part

    # 方法二:BFS
    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                query = [i]
                visited.add(i)
                count += 1
                while query:
                    q = query.pop()
                    for adj in dic[q]:
                        if adj not in visited:
                            query.append(adj)
                            visited.add(adj)
        return count

    # 方法三:DFS
    def countComponents3(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        visited = [False] * n
        dic = defaultdict(list)
        count = 0
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])

        def dfs(node):
            if not visited[node]:
                visited[node] = True
                for adj in dic[node]:
                    dfs(adj)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
