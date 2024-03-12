# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/8 9:03'

import time


class Solution:
    # 方法一:先求总和再根据是否重叠来减去重复计算部分
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def isoverlap(leftxa, rightxa, leftxb, rightxb):
            return max(leftxa, leftxb) < min(rightxa, rightxb)

        ans = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)

        if isoverlap(ax1, ax2, bx1, bx2) and isoverlap(ay1, ay2, by1, by2):
            ans -= (min(bx2, ax2) - max(bx1, ax1)) * (min(by2, ay2) - max(by1, ay1))
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
