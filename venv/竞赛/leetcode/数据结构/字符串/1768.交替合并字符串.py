# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 14:35'

import time


class Solution:
    # 方法一:双指针
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        ans = ""
        while p < min(len(word1), len(word2)):
            ans += word1[p] + word2[p]
            p += 1
        if len(word1) > len(word2):
            ans += word1[p:]
        else:
            ans += word2[p:]
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
