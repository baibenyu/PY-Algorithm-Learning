# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 9:10'
from typing import List


class Solution:
    # 方法一:动态规划--优化方案,因为每一个值都只需要上一层和本层就能推出,且不会重复使用,所以可以直接原地修改
    # 到某个坐标点的最小路径和,等于上方和左方坐标点,小的那个坐标点路径和+自身数字--分解成更小的子问题
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]
