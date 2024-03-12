# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 8:33'

import time
from typing import List


class Solution:
    # 方法一:DP
    # 审题-->发现所谓连线(即匹配相同数字)不能相交,实际上就是在说数字序列匹配时不能颠倒数字的相对顺序(最长公共子序列类)
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 == num2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
