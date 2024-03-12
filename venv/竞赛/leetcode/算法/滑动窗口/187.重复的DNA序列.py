# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/24 19:21'

import time
from collections import defaultdict
from typing import List

L = 10
bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


class Solution:
    # 方法一:哈希表+滑动窗口+位运算
    # 用32位中的低20位来表示长度为10的字符串
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)  # 滑动窗口右移,或上当前新字符,取低20位比特
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i: i + L])
        return ans

    # 方法二:哈希表
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        cnt = defaultdict(int)
        for i in range(len(s) - L + 1):
            sub = s[i: i + L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
