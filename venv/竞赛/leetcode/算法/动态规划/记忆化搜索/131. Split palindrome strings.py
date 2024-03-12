# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 16:12'

import time
from typing import List


class Solution:
    # 方法一:回溯+记忆化搜索
    def partition(self, s: str) -> List[List[str]]:
        import functools

        n = len(s)
        ret = list()
        ans = list()

        @functools.lru_cache
        def isPalindrome(i: int, j: int) -> bool:  # 记忆化判断子串是否为回文串
            if i >= j:
                return True
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else False

        def dfs(i: int):  # 回溯尝试所有切割出来的子串是否为回文串
            if i == n:
                ret.append(ans.copy())
                return

            for j in range(i, n):
                if isPalindrome(i, j):
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
