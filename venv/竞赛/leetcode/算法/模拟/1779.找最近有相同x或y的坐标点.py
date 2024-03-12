# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 9:15'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance = float("inf")
        index = -1
        for i in range(len(points)):
            if points[i][0] == x and abs(y-points[i][1]) < distance:
                distance = abs(y-points[i][1])
                index = i
            elif points[i][1] == y and abs(x-points[i][0]) < distance:
                distance = abs(x-points[i][0])
                index = i
        return index
if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
