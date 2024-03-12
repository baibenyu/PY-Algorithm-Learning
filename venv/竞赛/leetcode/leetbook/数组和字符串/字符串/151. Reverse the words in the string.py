# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 7:41'

import time


class Solution:
    # 方法一:模拟
    def reverseWords(self, s: str) -> str:
        string = s.strip().split()
        string.reverse()
        ans = ""
        for each in string[:-1]:
            ans += each + " "
        ans += string[-1]
        return ans

    # 方法二:API
    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.split()[::-1])  # join前面的字符表示以什么作为间隔


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
