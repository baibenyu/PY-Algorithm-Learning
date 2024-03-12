# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/12 16:27'

import time


class Solution:
    # 方法一:DP--字符串匹配问题
    # dp[i][j]表示s的前i个字符能不能匹配p的前j个字符
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':  # 除非一直为*,否则不可能为TRUE
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':  # 若为*则可通过p的前j-1个字符匹配s的前i个字符(用),可通过p的前j个字符匹配s的前i-1个字符(不用)
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]  # 用 or 不用
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

    # 方法二:贪心+AC自动机
    # 当有多个*号时,完全可以转化为在s中寻找p中的字母模式,优先匹配这些字母,因为其它都可以被*匹配
    # 1.*a*b* -- 以*开头,以*结尾
    # 2.*a*b -- 以*开头,不以*结尾--->匹配最后一个*之后的内容,转化为情况1
    # 3.a*b* -- 不以*开头,以*结尾--->匹配第一个*之前的内容,转化为情况1
    def isMatch2(self, s: str, p: str) -> bool:
        def allStars(st: str, left: int, right: int) -> bool:
            return all(st[i] == '*' for i in range(left, right))

        def charMatch(u: str, v: str) -> bool:
            return u == v or v == '?'

        sRight, pRight = len(s), len(p)
        while sRight > 0 and pRight > 0 and p[pRight - 1] != '*':
            if charMatch(s[sRight - 1], p[pRight - 1]):
                sRight -= 1
                pRight -= 1
            else:
                return False

        if pRight == 0:
            return sRight == 0

        sIndex, pIndex = 0, 0
        sRecord, pRecord = -1, -1
        while sIndex < sRight and pIndex < pRight:
            if p[pIndex] == '*':
                pIndex += 1
                sRecord, pRecord = sIndex, pIndex
            elif charMatch(s[sIndex], p[pIndex]):
                sIndex += 1
                pIndex += 1
            elif sRecord != -1 and sRecord + 1 < sRight:
                sRecord += 1
                sIndex, pIndex = sRecord, pRecord
            else:
                return False

        return allStars(p, pIndex, pRight)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
