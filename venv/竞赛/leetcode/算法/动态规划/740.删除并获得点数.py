# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 15:56'

import time
from typing import List


class Solution:
    # 方法一:动态规划
    # 类似rob,即选了前一个就不能选后一个,所以当前的最大值 = max(选前一个的最大值,不选前一个选更前一个+当前值)
    def deleteAndEarn(self, nums: List[int]) -> int:
        import collections
        nums.sort()
        c1 = collections.Counter(nums)
        maxnum = max(c1)
        c2 = [0 for i in range(maxnum + 1)]
        species = len(c1)
        for key in c1:
            c2[key] = c1[key] * key
        if species < 2:
            return c2[maxnum]
        else:
            dp = [0 for _ in range(maxnum + 1)]
            dp[0] = c2[0]
            dp[1] = max(c2[0], c2[1])
            for i in range(2, maxnum + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + c2[i])
            return max(dp)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
