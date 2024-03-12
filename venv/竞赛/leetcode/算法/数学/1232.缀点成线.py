# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 20:16'

import time
from typing import List


class Solution:
    # 方法一:求斜率
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        k = None
        prek = k
        i = 1
        while i < len(coordinates):
            x = coordinates[i][0] - coordinates[i - 1][0]
            y = coordinates[i][1] - coordinates[i - 1][1]
            if x == 0:
                k = float("inf")
            else:
                k = y / x
            if prek:
                if prek != k:
                    return False
            else:
                prek = k
            i += 1
        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
