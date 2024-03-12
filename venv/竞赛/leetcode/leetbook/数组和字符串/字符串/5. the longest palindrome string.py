# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 9:21'

import time


class Solution:
    # 方法一:中心扩展法
    def __init__(self):
        self.res = ""

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i - 1:
                self.res = s[i + 1:j]

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res

    # 方法二:manacher算法
    # 在原算法基础上多记录了最大半径回文子串的中心
    def longestPalindrome2(self, s: str) -> str:

        def manacherstring(string: str):
            s1 = "#"
            for x in range(len(string)):
                s1 += string[x]
                s1 += "#"
            return s1

        if not s or len(s) == 0:
            return ""
        else:
            string = manacherstring(s)
            length = len(string)
            r_array = [0 for _ in range(length)]
            center, rlimit = -1, -1
            max_r = float("-inf")
            max_c = -1
            for i in range(length):
                if rlimit > i:
                    r_array[i] = min(r_array[2 * center - i], rlimit - i)
                else:
                    r_array[i] = 1
                while i + r_array[i] < length and i - r_array[i] > -1:
                    if string[i + r_array[i]] == string[i - r_array[i]]:
                        r_array[i] += 1
                    else:
                        break
                if i + r_array[i] > rlimit:
                    rlimit = i + r_array[i]
                    center = i
                if max_r < r_array[i]:
                    max_r = r_array[i]
                    max_c = i
            ori_c = max_c // 2  # 原回文串中心
            ori_r = (max_r - 1) // 2  # 原回文串半径
            return s[ori_c - ori_r:ori_c + max_r - 1 - ori_r]  # 右边界是开区间

    # 方法三:DP
    # 一个字符串是否是回文串可以由内部子串是否是回文串以及两端字符是否相等来等价表示
    def longestPalindrome3(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
