# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 16:21'

import time
from typing import List


class NumMatrix:
    # 方法一:二维前缀和
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums

        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
