# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/8 9:09'

import time


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])  # 行,列
        self.count = 0  # 记录有几个集合
        self.parent = [-1 for _ in range(m*n)]
        self.rank = [0 for _ in range(m*n)]  # 记录集合的秩
        for i in range(m):
            for j in range(n):
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
            self.areas[rootx] += self.areas[rooty]
            self.areas[rooty] = self.areas[rootx]
            if self.rank[rootx] == self.rank[rooty]:  # 若被合并集合的秩一样大,那么就让合并集合的秩+1
                self.rank[rootx] += 1
            self.count -= 1  # 减少集合数,因为被合并了
            return True
        else:
            return False

    def getCount(self):
        return self.count


if __name__ == '__main__':
    start = time.perf_counter()
    """
    1.岛问题--找有几个连续的陆地
    解:[1]BFS[2]DFS
    [3]进阶--并查集Union
    
    """
    end = time.perf_counter()
    print(end - start)
