# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/10 8:10'

import time


class Solution:
    # 方法一:DFS--从左往右依次取递增个单词
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(l, r):
            nonlocal ans, visited
            if l == len(s):
                ans = max(len(visited), ans)
                return
            for r in range(l + 1, len(s) + 1):
                if s[l:r] not in visited:
                    visited.add(s[l:r])
                    dfs(r, r + 1)
                    visited.remove(s[l:r])

        ans = 0
        visited = set()
        dfs(0, 1)
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
