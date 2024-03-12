# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 8:50'

import time


class Solution(object):
    # 方法一:DP
    # dp[i][j]表示前i-1个字符和前j-1个字符的最大子序列ascii值的和
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        def get_total_ascii(s):
            return sum([ord(c) for c in s])

        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return get_total_ascii(s1) + get_total_ascii(s2) - 2 * dp[-1][-1]  # 删除的ascii值 = 总asci值-保留的ascii值


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
