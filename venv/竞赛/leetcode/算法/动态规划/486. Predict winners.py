# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 15:54'

import time
from typing import List


class Solution:
    # 方法一:DP
    # dp[i][j]表示在[i,j]之间,先手对后手的相对净胜分
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(nums):  # 初始化:仅有一个数字差距固定
            dp[i][i] = num
        # 甲面对区间[i...j]时，
        #   如果甲拿nums[i]，那么变成乙面对区间[i+1...j]，这段区间内乙对甲的净胜分为dp[i+1][j]；那么甲对乙的净胜分就应该是nums[i] - dp[i+1][j]。
        #   如果甲拿nums[j]，同理可得甲对乙的净胜分为是nums[j] - dp[i][j-1]。
        for i in range(length - 2, -1, -1):  # 转移方程中用到i+1,所以要逆序遍历
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
