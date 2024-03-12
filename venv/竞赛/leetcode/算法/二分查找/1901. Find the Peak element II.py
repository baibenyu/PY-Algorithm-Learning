# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 21:32'

import time
from typing import List


class Solution:
    # 方法一:二分查找--题目只要求找到极大值,不要求按顺序找
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])

        # 找到单列中最大值和其索引
        def getColMax(i: int) -> (int, int):  # 保证取到的值大于上方和下方
            value, index = mat[0][i], 0
            for row in range(1, m):
                if mat[row][i] > value:
                    value, index = mat[row][i], row
            return value, index

        # 二分法切片
        left, right = 0, n - 1
        while left < right:
            mid = left + int((right - left) / 2)
            max_val, max_idx = getColMax(mid)
            if mid == 0:  # left = 0, right = 1
                if max_val > mat[max_idx][1]:
                    return [max_idx, 0]
                else:
                    left = 1
            else:
                if mat[max_idx][mid - 1] < max_val and mat[max_idx][mid + 1] < max_val:  # 满足大于左右时返回值
                    return [max_idx, mid]
                elif mat[max_idx][mid - 1] < max_val < mat[max_idx][mid + 1]:  # 大于左小于右时,不应该向左因为左边小于当前值,向右才可能符合条件
                    left = mid + 1
                else:  # 同上,方向换一下
                    right = mid - 1

        # 对于最后剩下的一列，其最大值一定是极大值
        _, idx = getColMax(left)  # 由左向右保证了当前值大于左边,右边为-1,又是列中的最大值,大于上下方
        return [idx, left]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
