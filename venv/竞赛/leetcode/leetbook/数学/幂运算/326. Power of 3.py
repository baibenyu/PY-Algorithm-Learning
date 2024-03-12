# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/7 7:52'

import time


class Solution:
    # 方法一:打表--利用数据范围内3的最大幂数,所有3的幂都能被最大幂整除
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

    # 方法二:模拟--依次除以三,观察最后余数是否为1
    def isPowerOfThree2(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
