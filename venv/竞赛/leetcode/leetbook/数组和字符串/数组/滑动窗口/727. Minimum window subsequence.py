# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/22 9:23'

import time


class Solution:
    # 方法一:滑动窗口--顺序增长,逆序缩短
    def minWindow(self, s1: str, s2: str) -> str:
        i, j = 0, 0
        min_len = float('inf')
        left, right = 0, 0
        while i < len(s1):
            if s1[i] == s2[j]:
                j += 1
            # 完成了匹配
            if j == len(s2):
                right = i
                j -= 1
                while j >= 0:  # 逆序匹配找到左边界
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1
                if right - i + 1 < min_len:
                    left = i
                    min_len = right - left + 1
                j = 0
            i += 1
        if min_len != float('inf'):
            return s1[left: left + min_len]
        return ""


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
