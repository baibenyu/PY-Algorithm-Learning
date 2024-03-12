# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/2 16:28'
from typing import List


class Solution:
    # 方法一:暴力,遍历所有区间看他们的右边界是否超过后续会议的左边界
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        length = len(intervals)
        ans = [1] * length
        for j in range(length):
            right = intervals[j][1]
            for i in range(j + 1, length):
                if right > intervals[i][0]:
                    ans[i] += 1

        return max(ans)

    # 方法二:优先队列,最小堆
    # 实际上蕴含的逻辑是,在已知所有会议的结束时间时,新会议若要开始,应该查看最早结束的会议是否结束,若结束则出堆,若还没结束则排队
    # 最早结束时间实际上就是最小值,即我们要维持一个随时间变化能让最小值在最前面的数据结构--小根堆
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort(key = lambda x: x[0])
        ans = []
        heapq.heappush(ans, intervals[0][1])
        for i in intervals[1:]:
            if i[0] >= ans[0]:
                heapq.heappop(ans)
            heapq.heappush(ans, i[1])
        return len(ans)
