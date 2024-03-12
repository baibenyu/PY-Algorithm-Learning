# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 21:04'
import bisect
from typing import List


class Solution:
    # 方法一:二分查找
    # 对每一行都应用二分查找
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False

    # 方法二:z型查找
    # 从以(x,y)为右上角的矩形开始查找,因为矩阵行和列都是升序排序的,意味着右上角既是行的最大值,也是列的最小值
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:  # 从右上开始判断
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:  # 若大于target,说明这一列下面都大于target,判断的列数-1,上面的值已经判断过了
                y -= 1
            else:  # 若小于target,说明这一行左边都小于target,行数+1,右边已经判断过了
                x += 1
        return False
