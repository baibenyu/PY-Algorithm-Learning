# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/17 10:24'

import time
from bisect import bisect
from typing import List


class Solution(object):
    # 方法一:二次二分
    # 先0列查找合适的行,再在该行中查找该数
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        target_row = bisect.bisect_right(col0, target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col >= N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

    # 方法二:合并,一次二分
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            x, y = mid // n, mid % n
            if matrix[x][y] > target:
                r = mid - 1
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                return True
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
