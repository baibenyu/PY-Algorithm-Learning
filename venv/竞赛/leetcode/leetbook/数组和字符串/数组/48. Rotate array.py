# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 10:24'
from typing import List


class Solution:
    # 方法一:找规律,会发现转90度实际上只对矩阵的左上角四分之一旋转,找到坐标对应关系
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):  # 当n为奇数时,列数要比行数多一,偶数则相同
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
    # 方法二:用辅助数组存储不同方式遍历矩阵,然后再用新矩阵覆盖原矩阵
