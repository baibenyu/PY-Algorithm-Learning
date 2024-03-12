# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 12:01'

import time


class Solution:
    # 方法一:贪心+双指针
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    # 方法二:DP
    # dp表示从i位置开始第一次出现j的下标,在判断是否有某个字符时就可以直接O(1)访问
    def isSubsequence2(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
