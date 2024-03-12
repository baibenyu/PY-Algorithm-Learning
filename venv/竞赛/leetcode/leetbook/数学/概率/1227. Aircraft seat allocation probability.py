# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/7 9:17'

import time


class Solution:
    # 方法一:动态规划--推导出f(n) = 1 if n == 1  ;
    #                         = 0.5 if n == 2 ;
    #                         = f(n-1) if n >= 3
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
