# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/1 21:00'

class Solution:
    # 方法一:DP
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):  # 移动原字符串
            for j in range(1, n + 1):
                if p[j - 1] == '*':  # 如果当前为*,转移到*的匹配整体之前的状态,即p字符串之前字符的状态
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]  # 匹配s字符串的相同字符一个,并且继续使用*号匹配
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]
