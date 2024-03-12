# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 16:25'

import time


class Solution:
    # 方法一:DP--二次
    # g[i][j]表示该子串是否为回文串
    # f[i]表示前i个字符最少需要切割几次才能是得到的均为回文串
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:  # 无需切割,自身即为回文串
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:  # 0已经在if中检测了,若j+1到i为回文串,则在f[j]基础上多切割一次
                        f[i] = min(f[i], f[j] + 1)

        return f[n - 1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
