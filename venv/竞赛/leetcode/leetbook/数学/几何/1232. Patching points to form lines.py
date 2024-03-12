# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/8 9:38'

import time
from typing import List


class Solution:
    # 方法一:分类讨论--先解决斜率为0及不存在的情况
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if all(True if each[0] == coordinates[0][0] else False for each in coordinates) or all(
                True if each[1] == coordinates[0][1] else False for each in coordinates):
            return True

        x1, y1, x2, y2 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
        if x2 - x1 == 0 or y2 - y1 == 0:
            return False
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        for i in range(2, len(coordinates)):
            if coordinates[i][1] != a * coordinates[i][0] + b:
                return False
        return True


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
