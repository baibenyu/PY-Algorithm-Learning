# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 8:46'

import time
from collections import Counter
from typing import List, Tuple


class Solution:
    # 方法一:正方形的四边长相等,且对角线相等,对角线长度=边长*根号二
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        d = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]  # 求出所有边长
        cnt = Counter(d)
        dst = sorted(cnt)
        return True if cnt[dst[0]] == 4 and cnt[dst[1]] == 2 and dst[0] * 2 == dst[1] else False

    # 方法二:对角线中点相等->平行四边形,对角线长度相等->矩形,对角线互相垂直->正方形
    def validSquare2(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def checkLength(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
            return v1[0] * v1[0] + v1[1] * v1[1] == v2[0] * v2[0] + v2[1] * v2[1]

        def checkMidPoint(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
            return p1[0] + p2[0] == p3[0] + p4[0] and p1[1] + p2[1] == p3[1] + p4[1]

        def calCos(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
            return v1[0] * v2[0] + v1[1] * v2[1]

        def help(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
            v1 = (p1[0] - p2[0], p1[1] - p2[1])
            v2 = (p3[0] - p4[0], p3[1] - p4[1])
            return checkMidPoint(p1, p2, p3, p4) and checkLength(v1, v2) and calCos(v1, v2) == 0

        if p1 == p2:
            return False
        if help(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if help(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if help(p1, p4, p2, p3):
            return True
            return False

if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
