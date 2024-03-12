# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/16 21:38'

import time

start = time.clock()


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])  # 行,列
        self.count = 0  # 记录有几个集合
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)  # 记录集合的秩
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
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


m, n = map(int, input().strip().split())
k = int(input().strip())
matrix = [[1 for _ in range(n)] for _ in range(m)]
uf = UnionFind(matrix)
for i in range(k):
    a, b = map(int, input().strip().split())
    uf.union(a - 1, b - 1)
print(uf.getCount())

end = time.clock()
print(end - start)
