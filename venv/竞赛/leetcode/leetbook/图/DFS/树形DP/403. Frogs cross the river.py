# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/18 9:43'

import time
from functools import lru_cache
from typing import List


class Solution:
    # 方法一:DFS记忆化搜索--枚举+记忆
    def canCross(self, stones: List[int]) -> bool:
        @lru_cache(None)
        def dfs(pos, step):
            if pos == stones[-1]:
                return True
            for d in [-1, 0, 1]:
                if step + d > 0 and pos + step + d in set(stones):
                    if dfs(pos + step + d, step + d):
                        return True
            return False

        pos, step = 0, 0
        return dfs(pos, step)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
