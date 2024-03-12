# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 14:20'

import time


class Solution:
    # 方法一:DP
    # dp表示当前值能取到的最大乘积
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])  # 分别转移自1.自己 2.仅拆成两个数 3.拆出多个数,利用之前拆分出的最大结果,在这个基础上继续乘上
        return dp[n]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
