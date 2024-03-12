# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 16:20'
import collections
import time
from typing import List


class Solution:
    # 方法一:DFS+哈希表
    # 利用字典存储多叉树,再用DFS遍历根结点到叶子结点的路径,取路径最长
    def __init__(self):
        self.son = collections.defaultdict(list)

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        for i in range(n):
            if i != headID:
                self.son[manager[i]].append(i)

        return self.dfs(headID, informTime)

    def dfs(self, u, informTime):
        res = 0
        for s in self.son[u]:
            res = max(res, informTime[u] + self.dfs(s, informTime))
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
