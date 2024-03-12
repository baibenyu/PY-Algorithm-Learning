# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/7 7:31'

import time


class Solution:
    # 方法一:位运算--与运算的性质
    # a & (a -1)的结果为将a的二进制表示的最后一个1变成0;
    # 若为2的整数次幂,必然二进制只含有一个1
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n & (n - 1) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
