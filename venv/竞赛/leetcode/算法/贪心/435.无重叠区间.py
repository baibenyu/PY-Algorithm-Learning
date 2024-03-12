# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/17 9:52'

import time
from typing import List


class Solution:
    # 方法一:贪心
    # 要最多的不重叠区间,就意味着每个区间的跨度应该尽可能的小,而左边界从0开始,跨度大的区间的右边界一定很大
    # 右边界小的区间跨度一定小,所以将右边界从小到大排序,依次取不重叠的区间,那么最后取到的即为最多不重叠区间数量
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]

        return n - ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
