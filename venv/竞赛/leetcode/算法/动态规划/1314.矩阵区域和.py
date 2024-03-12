# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 16:12'

import time
from typing import List


class Solution:
    # 方法一:二维前缀和
    # 当前前缀和 = 少一行的前缀和+少一列的前缀和-重复的左上角部分前缀和+右下角的值
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x, y):  # 限制边界
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):  # 同理只不过加减颠倒一下
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K,
                                                                                                            j - K)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
