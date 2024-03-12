# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 16:16'

import time
from typing import List


class Solution:
    # 方法一:动态规划
    # dp维护一个能跳到的最远值,若最远值小于等于当前位置,说明当前位置之后的不可达
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 1:
            return True
        else:
            dp = [0 for _ in range(length)]
            dp[0] = nums[0]
            for i in range(length - 1):
                dp[i] = max(dp[i - 1], i + nums[i])
                if dp[i] <= i:
                    return False
            return True if dp[length - 2] >= length - 1 else False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
