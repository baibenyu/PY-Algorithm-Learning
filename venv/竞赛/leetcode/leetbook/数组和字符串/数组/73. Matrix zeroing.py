# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/25 10:50'

import time
from typing import List


class Solution:
    # 方法一:用数组记录记录0出现的行和列
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.append(j)
                    rows.append(i)
        for each in rows:
            matrix[each] = [0 for _ in range(len(matrix[0]))]
        for each in cols:
            for i in range(len(matrix)):
                matrix[i][each] = 0

    # 方法二:利用数组的第一行和第一列记录其它行列的是否应该被置0,用两个额外变量标记第一行和第一列是否含0
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
