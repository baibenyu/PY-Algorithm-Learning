# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/7 19:17'

import time
from typing import List


class Solution:
    # 方法一:排序+双指针
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        ans = []
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            left = max(slots1[p1][0], slots2[p2][0])
            if slots1[p1][1] <= slots2[p2][1]:
                right = slots1[p1][1]
                if right - left >= duration:
                    return [left, left + duration]
                p1 += 1
            else:
                right = slots2[p2][1]
                if right - left >= duration:
                    return [left, left + duration]
                p2 += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
