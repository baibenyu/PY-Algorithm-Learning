# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 14:13'

import time
from typing import List


class Solution:
    # 方法一:DP
    # 完全背包
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
