# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 14:25'

import time
from typing import List


class Solution:
    # 方法一:动态规划
    # 碰到当前元素会改变原子数组的正负性,根据这个性质来递推
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        if nums[0] > 0:
            dp[0][0] = 1
        elif nums[0] < 0:
            dp[0][1] = 1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i - 1][1] != 0:  # 遇到前驱为0,需要特殊处理,此处是因为已经初始化为0
                    dp[i][1] = dp[i - 1][1] + 1
            elif nums[i] < 0:
                if dp[i - 1][1] != 0:
                    dp[i][0] = dp[i - 1][1] + 1
                if dp[i - 1][0] != 0:
                    dp[i][1] = dp[i - 1][0] + 1
                else:
                    dp[i][1] = 1
        return max([x[0] for x in dp])


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
