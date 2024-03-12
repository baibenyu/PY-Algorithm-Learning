# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 9:29'

import time


class Solution:
    # 方法一:DP
    # dp表示[i,j]范围内的最大回文子序列
    # 确保0-n的结果最后出,所以逆序遍历
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:  # 中心扩展
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:  # 考虑了偶数
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
