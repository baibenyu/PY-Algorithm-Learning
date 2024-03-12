# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/23 10:39'

import time
from typing import List


class Solution:
    # 方法一:枚举
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for item in grid:
            for num in item:
                if num < 0:
                    total += 1

        return total

    # 方法二:z形查找
    def countNegatives2(self, grid: List[List[int]]) -> int:
        total = 0
        i, j = 0, len(grid[0]) - 1

        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                total += len(grid) - i
                j -= 1
        return total


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
