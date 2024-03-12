# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 11:12'
from typing import List


class Solution:
    # 方法一:动态规划,将字符串减少一个字符,问题规模变小但仍是相同问题
    # dp[i] 表示 s 的前 i 位是否可以用 wordDictwordDict 中的单词表示
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):  # s[i,⋯,j) 出现在 wordDictwordDict 中，说明 s 的后 j 位可以表示
                    dp[j] = True
        return dp[-1]

    # 方法二:记忆化搜索
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)
