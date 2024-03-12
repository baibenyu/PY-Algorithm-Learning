# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/21 20:44'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 最多旋转 4 次
        for k in range(4):
            # 旋转操作
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    mat[i][j], mat[n - 1 - j][i], mat[n - 1 - i][n - 1 - j], mat[j][n - 1 - i] \
                        = mat[n - 1 - j][i], mat[n - 1 - i][n - 1 - j], mat[j][n - 1 - i], mat[i][j]

            if mat == target:
                return True
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
