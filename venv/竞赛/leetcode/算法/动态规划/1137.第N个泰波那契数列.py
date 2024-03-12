# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 20:18'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 1, 1
            for i in range(n - 2):
                temp = a
                a = b
                b = c
                c = temp + a + b
            return c

    # 方法二:矩阵快速幂
    # 斐波那契数列同理
    def tribonacci2(self, n: int) -> int:
        if n < 2:
            return n
        q = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]  # 手写按原规律生成矩阵,所求的q即为这个矩阵
        ans = self.matrix_pow(q, n - 1)
        return ans[0][0]

    def matrix_pow(self, matrix: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1], [1], [0]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(ret, matrix)
            n >>= 1
            matrix = self.matrix_multiply(matrix, matrix)
        return ret

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
