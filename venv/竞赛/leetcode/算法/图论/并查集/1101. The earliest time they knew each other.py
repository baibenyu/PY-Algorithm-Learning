# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 9:01'

import time


# 并查集模板
class UnionFind:
    def __init__(self, size):
        self._father = {}
        for i in range(size):
            self._father[i] = i
        self._num_of_set = size

    def add(self, x):
        if x not in self._father:
            self._father[x] = x

    def find(self, x):
        root = x
        while self._father[root] != root:
            root = self._father[root]

        # 路径压缩
        while x != root:
            origin_root = self._father[x]
            self._father[x] = root
            x = origin_root

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self._father[root_x] = root_y
            self._num_of_set -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_count(self):
        return self._num_of_set


class Solution(object):
    # 方法一:按时间排序+并查集
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        uf = UnionFind(N)
        logs = sorted(logs, key = lambda x: x[0])
        for time, x, y in logs:
            uf.merge(x, y)
            if uf.get_count() == 1:
                return time
        return -1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
