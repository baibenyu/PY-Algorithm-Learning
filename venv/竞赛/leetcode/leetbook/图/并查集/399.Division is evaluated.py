# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 19:48'
from typing import List


class UnionFind(object):
    def __init__(self, k):
        self.parent = [i for i in range(k)]
        # weight节点指向父节点的权值
        self.weight = [1.0 for _ in range(k)]

    def find(self, x):
        # 路径压缩，找到对应点x的根节点
        if x != self.parent[x]:
            # 如果当前节点的根节点不是自己，则还没有到根节点，递归查根节点
            origin_parent = self.parent[x]
            root_y = self.find(self.parent[x])
            self.parent[x] = root_y
            self.weight[x] *= self.weight[origin_parent]
        else:
            root_y = x
        return root_y

    def union(self, v1, v2, weight):
        # 在树中合并两个变量
        # 先找到两个变量的根节点
        root_v1 = self.find(v1)
        root_v2 = self.find(v2)
        if root_v1 != root_v2:
            # 根节点不相同执行合并操作
            # 把其中一个根节点的父节点指向另一个节点的根节点
            self.parent[root_v1] = root_v2
            # 更新权重
            self.weight[root_v1] = self.weight[v2] * weight / self.weight[v1]

    def is_connected(self, id1, id2):
        # 先找到两个变量的根节点
        root_v1 = self.find(id1)
        root_v2 = self.find(id2)
        if root_v1 == root_v2:
            # 连接同一个根，则返回权重比例
            return self.weight[id1] / self.weight[id2]
        else:
            return -1.0


class Solution(object):
    # 方法一:并查集
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        union_find = UnionFind(2 * n)
        # 变量字典，存储变量对应的索引
        var_dic = {}
        num = 0
        for i in range(n):
            var1, var2 = equations[i][0], equations[i][1]
            if var1 not in var_dic:
                var_dic[var1] = num
                num += 1
            if var2 not in var_dic:
                var_dic[var2] = num
                num += 1
            # 将两个变量做合并操作
            union_find.union(var_dic[var1], var_dic[var2], values[i])

        # 查询
        m = len(queries)
        res = []
        for i in range(m):
            var1, var2 = queries[i][0], queries[i][1]
            var1_id1 = var_dic.get(var1)
            var1_id2 = var_dic.get(var2)
            if var1_id1 is None or var1_id2 is None:
                # 有一个变量不存在，返回-1
                res.append(-1.0)
            else:
                # 两个变量到根节点权重的比值
                res.append(union_find.is_connected(var1_id1, var1_id2))
        return res
