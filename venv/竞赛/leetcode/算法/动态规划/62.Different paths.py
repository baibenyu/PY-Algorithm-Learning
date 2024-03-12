# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 9:52'
from math import comb


class Solution:
    # 方法一:动态规划,每个坐标的方案数都等于上方的方案数+左方的方案数
    # 将边界条件拿出来处理,用二维矩阵比用字典更快
    def uniquePaths(self, m: int, n: int) -> int:
        dp = dict()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:  # 起始条件和边界条件
                    dp[(i, j)] = 1
                else:  # 一般情况
                    dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - 1)]
        return dp[(m - 1, n - 1)]

    # 方法二:数学--组合
    # 总共走m+n-2步,其中n-1步向右
    def uniquePaths2(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)
