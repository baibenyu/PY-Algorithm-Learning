# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 19:30'

import time
from typing import List


class Solution:
    # 方法一:动态规划,因为每一项都只由前两项推出,所以无需存储整个数组
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for i in range(1, n):
                c = a + b
                a = b
                b = c
            return c

    # 方法二:矩阵快速幂,f(n) = [[1, 1], [1, 0]]^n * [1,0]
    def fib2(self, n: int) -> int:
        if n < 2:
            return n
        q = [[1, 1], [1, 0]]
        ans = self.matrix_pow(q, n - 1)
        return ans[0][0]

    def matrix_pow(self, matrix: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1], [0]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(ret, matrix)
            n >>= 1
            matrix = self.matrix_multiply(matrix, matrix)
        return ret

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0], [0, 0]]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
