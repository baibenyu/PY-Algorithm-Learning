# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/4 9:48'

import time


class Solution:
    # 方法一:DP
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':  # 由第i位(i-1是下标)数字单独进行映射
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:  # 由i和i-1为数字进行映射,不能以0开头且小于26
                f[i] += f[i - 2]
        return f[n]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
