# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 16:40'

import time
from functools import lru_cache
from typing import List


class Solution:
    # 方法一:记忆化搜索
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:  # 处于需要旅游的日子
                return min(dp(i + d) + c for c, d in zip(costs, durations))  # 取三种决策中花费最少的
            else:  # 无需旅游则无需花费
                return dp(i + 1)

        return dp(1)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
