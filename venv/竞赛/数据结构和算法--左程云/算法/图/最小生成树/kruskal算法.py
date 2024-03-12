# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/5 15:43'

import time
import heapq


class Edge:  # 带权值的边
    def __init__(self, weight, begin, to):
        self.weight = weight
        self.begin = begin
        self.to = to


class Graph:  # 图,数字与结构之间的连接
    def __init__(self):
        self.nodes = dict()  # 由数字得到具体几号结点
        self.edges = set()  # 结点与哪些其它结点的连接


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
            return True
        else:
            return False

    def getCount(self):
        return self.count


# 注意:要求无向图!!!
def kruskal(matrix):  # 具体思想:每次选取最小权值的边,如果边的两头不处于同一集合,那么合并,说明该边必须且最小,若已处于同一集合,说明该边多余
    uf = UnionFind(matrix)
    q = list()
    heapq.heapify(q)
    graph = Graph()
    for each in graph.edges:
        heapq.heappush(q, each)
    res = []
    while q:
        edge = heapq.heappop(q)
        if uf.union(edge.begin, edge.to):
            res.append(edge)
    return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
