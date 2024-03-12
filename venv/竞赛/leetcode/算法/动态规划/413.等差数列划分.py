# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/4 9:17'

import time
from typing import List


class Solution:
    # 方法一:DP
    # dp0表示有几个连续的公差相等,dp1表示目前为止的成等差数列的子数组个数
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return 0

        dp = [[0, 0] for _ in range(length)]
        dp[1][0] = 1
        for i in range(2, length):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i][0] > 1:
                    dp[i][1] = dp[i - 1][1] + dp[i][0] - 1
            else:
                dp[i][0] = 1
        count = 0
        for j in range(2, length):
            if dp[j][1] > dp[j - 1][1]:
                if j == length - 1:
                    count += dp[j][1]
            else:
                count += dp[j - 1][1]
        return count

    # 方法二:差分+计数
    def numberOfArithmeticSlices2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        d, t = nums[0] - nums[1], 0
        ans = 0

        # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
