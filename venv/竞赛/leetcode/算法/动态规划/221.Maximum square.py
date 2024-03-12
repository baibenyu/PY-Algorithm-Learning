# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 20:46'
from typing import List


class Solution:
    # 方法一:动态规划
    # dp[i][j]表示以(i,j)坐标为右下角的正方形的最大边长
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:  # 对于0行或0列的正方形来说,边长只能为1,否则越界了
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                        # 等于以左,左上,上三个为右下角的三角形中边长最小的值+1,详情请在纸上画出后可知
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide**2
        return maxSquare
