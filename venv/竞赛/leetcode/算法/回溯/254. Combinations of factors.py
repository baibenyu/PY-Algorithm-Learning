# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/18 19:32'

import time
from cmath import sqrt
from typing import List


class Solution:
    # 方法一:DFS
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, l):
            res = []
            for i in range(l, int(sqrt(n)) + 1):
                if n % i == 0:
                    res.append([i, n // i])
                    for sub in dfs(n // i, i):  # 递归地对非质因数分解,并加上当前的质因数i
                        res.append(sub + [i])
            return res

        return dfs(n, 2)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
