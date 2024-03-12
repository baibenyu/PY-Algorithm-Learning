# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 9:23'

import time


class Solution:
    # 方法一:KMP算法
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        fail = [-1] * n  # 建next数组
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1

        best = -1
        for i in range(n - 1, -1, -1):
            while best != -1 and s[best + 1] != s[i]:
                best = fail[best]
            if s[best + 1] == s[i]:
                best += 1

        add = ("" if best == n - 1 else s[best + 1:])
        return add[::-1] + s


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
