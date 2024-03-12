# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 9:15'

import time
from typing import List


class Solution:
    # 方法一:找到原矩阵和修改后矩阵的下标关系,直接覆盖即可
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n == r * c:
            matrix = [[0 for _ in range(c)] for _ in range(r)]
            for i in range(m):
                for j in range(n):
                    matrix[(i * n + j) // c][(i * n + j) % c] = mat[i][j]
            return matrix
        else:
            return mat


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
