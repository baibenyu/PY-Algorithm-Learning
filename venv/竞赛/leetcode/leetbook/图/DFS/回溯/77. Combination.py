# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/1 9:35'

import time
from typing import List


class Solution:
    # 方法一:回溯,组合问题都可以用回溯解决
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(n, k, StartIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res

    # 偷懒
    def combine2(self, n: int, k: int) -> List[List[int]]:
        import itertools
        return [list(x) for x in itertools.combinations([i for i in range(1, n + 1)], k)]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
