# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/9 19:33'

import time
from typing import List


class Solution:
    # 方法一:贪心+排序
    # 贪心--箭的排除范围最大化->当我们射出一支箭,该箭的最优位置应该在保证原气球被戳破的情况下,尽可能右移,换言之位置应该等于穿破气球中x坐标结束最早的气球的右边界
    # 排序--根据贪心原则的最优解情况下,每一只箭都应该射在某个气球的右边界上,根据右边界排序
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key = lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:  # 当无法处于新气球的区间时,应该更新箭枝的位置,并+1
                pos = balloon[1]
                ans += 1

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
