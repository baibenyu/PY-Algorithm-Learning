# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/21 7:31'

import time


class Solution:
    # 方法一:滑动窗口
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a", "e", "i", "o", "u"}
        ans = 0
        cur = 0
        for i in range(k):
            if s[i] in vowel:
                cur += 1
        ans = cur
        for j in range(k, len(s)):
            if s[j - k] in vowel:
                cur -= 1
            if s[j] in vowel:
                cur += 1
            ans = max(ans, cur)
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
