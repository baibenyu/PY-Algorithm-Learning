# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/23 8:44'

import time
from typing import List


class Solution:
    # 方法一:求连续子数组数目+限定条件
    # 我们知道 betweenK 可以直接利用 atMostK，即 atMostK(k1) - atMostK(k2 - 1)，其中 k1 > k2。
    # 我们知道如何求满足一定条件（这里是元素都小于等于 R）子数组的个数:而由于以索引为 i 结尾的子数组个数就是 i + 1，
    # 因此求连续子数组数目--可以直接用等差数列求和公式 (1 + n) * n / 2，其中 n 为数组长度
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        def notGreater(R):
            ans = cnt = 0
            for a in A:
                if a <= R:
                    cnt += 1
                else:
                    cnt = 0
                ans += cnt
            return ans

        return notGreater(R) - notGreater(L - 1)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
