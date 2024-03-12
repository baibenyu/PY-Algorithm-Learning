# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 12:14'

import time


class Solution(object):
    # 方法一:DP
    # dp表示t1的前i个字符和t2的前j个字符的最长公共子序列
    def longestCommonSubsequence(self, text1, text2):
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:  # 若M的第i个和N的第j个字符相等则直接在公共字符串上转移增长
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 否则等于M的前i-1个和N的前j个或者M的前i个和N的前j-1个中较大的那一个,即转移不变
        return dp[M][N]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
