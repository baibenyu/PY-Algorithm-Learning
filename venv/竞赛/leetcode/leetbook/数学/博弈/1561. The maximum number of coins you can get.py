# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 20:36'

import time
from typing import List


class Solution:
    # 方法一:贪心--每次选取最多的两堆+最少的一堆
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        cur = len(piles) - 2
        ans = 0
        for i in range(len(piles) // 3):
            ans += piles[cur]
            cur -= 2
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
