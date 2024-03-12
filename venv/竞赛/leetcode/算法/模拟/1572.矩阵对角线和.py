# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 20:55'

import time
from typing import List


class Solution:
    # 方法一:枚举
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        n = len(mat)
        ans = 0
        while i < n:
            ans += mat[i][i] + mat[i][n - i - 1]
            i += 1
        if n & 1:  # 奇数有重复
            return ans - mat[n // 2][n // 2]
        else:
            return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
