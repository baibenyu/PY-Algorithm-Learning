# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/1 11:21'
from typing import List


class Solution:
    # 方法一:排序
    # 先将区间数组根据区间的左边界升序排序,后再根据条件合并
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        ans = list()
        for i in range(1, len(intervals)):
            if right >= intervals[i][0]:
                if right < intervals[i][1]:
                    right = intervals[i][1]
            else:
                ans.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        ans.append([left, right])
        return ans
