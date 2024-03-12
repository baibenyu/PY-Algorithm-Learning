# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 18:54'
import collections
from typing import List


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])  # 行,列
        self.count = 0  # 记录有几个集合
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)  # 记录集合的秩
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j  # 初始化每个元素的父亲结点都是自己
                    self.count += 1  #

    def find(self, i):  # 找头结点
        if self.parent[i] != i:  # 如果自身的父结点不是自身,说明上层还有结点
            self.parent[i] = self.find(self.parent[i])  # 递归调用,查找父结点的父结点
        return self.parent[i]

    def union(self, x, y):  # 合并集合,是由头结点代表一个集合
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:  # 两个结点不在同一个集合中才能合并
            if self.rank[rootx] < self.rank[rooty]:  # 将集合合并到秩大的集合里,此处只是为了,让变量统一
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:  # 若被合并集合的秩一样大,那么就让合并集合的秩+1
                self.rank[rootx] += 1
            self.count -= 1  # 减少集合数,因为被合并了

    def getCount(self):
        return self.count


class Solution:
    # 方法一:并查集
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 上下左右都检查是否有1,若有就合并
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()


class Solution2:
    # 方法二:DFS,碰到1的时候向上下左右搜索是否存在1,若存在则继续遍历,直至无1
    def dfs(self, grid, r, c):
        grid[r][c] = 0  # 防止重复遍历
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands2(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands

    #  方法三:BFS,碰到1就先加入队列,直至遍历完上下左右后才弹出队列处理
    def numIslands3(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands
