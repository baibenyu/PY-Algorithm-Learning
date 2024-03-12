# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/7 8:13'

import time


class Solution:
    # 方法一:位运算--多一步判断1的位置是否奇数位
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n & (n - 1) == 0 and n & 2863311530 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
