# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 10:27'

import time


class Solution:
    # 方法一:双指针--找子序列
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while j < len(typed):
            if i < len(name) and typed[j] == name[i]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
