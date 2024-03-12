# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/4 10:40'

import time


class Solution:
    # 方法一:DP
    # 因为求最少的删除次数->求剩余公共部分最长 and 任意删除(顺序无所谓)->公共最长子序列
    # 两字符串长度-2*公共最长子序列长度,即最少删除次数
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[i - 1] == word2[j - 1]:  # 若M的第i个和N的第j个字符相等则直接在公共字符串上,转移增长
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 否则等于M的前i-1个和N的前j个或者M的前i个和N的前j-1个中较大的那一个,即转移不变

        return M + N - 2 * dp[M][N]

    # 方法二:DP
    # dp表示前i个和前j个最少删除次数
    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):  # 一者为空,则需要另一者的长度次删除
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # 不需要删除,转移不变
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1  # 较小的删除+1,转移增加

        return dp[m][n]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
