# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/15 8:37'

import time


class Solution:
    # 方法一:快速幂--注意当幂指数为负时,将底数转换为1/底数,就可将幂指数转正
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        ans = 1
        base = x
        index = n
        while index:
            if index % 2 == 1:
                ans *= base
            base = base ** 2
            index //= 2
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
