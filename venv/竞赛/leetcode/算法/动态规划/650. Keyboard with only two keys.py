# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 19:39'

import time


class Solution:
    # 方法一:DP
    # dp[i]表示要有i个A最少需要操作几次
    def minSteps(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = float("inf")
            j = 1
            while j * j <= i:
                if i % j == 0:
                    f[i] = min(f[i], f[j] + i // j)  # 同时从两边进行状态转移,i%j == 0,说明 i%(i//j) == 0
                    f[i] = min(f[i], f[i // j] + j)
                j += 1

        return f[n]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
