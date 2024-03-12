# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/6 19:22'
import heapq
from typing import List


class Solution:
    # 方法一:单调栈--单调递减
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        length = len(nums)
        q = collections.deque()  # 队列里存储的元素满足两个条件:1.必须在窗口范围内 2.在此时的窗口大小下有成为最大值的可能性
        ans = []
        for i in range(length):
            while q and nums[q[-1]] < nums[i]:  # 队列中的值必须遵守从大到小的规则,若要进入的元素比队尾元素大,出队直至元素比队尾小或空队
                q.pop()  # 本质上是在告诉队列里的元素,我比你大,你不可能是有我的窗口范围里的最大值
            q.append(i)
            if q[0] == i - k:  # 观察队头的元素是否过期,即窗口一直在滑动,每次都会弹出最窗口左边的元素,有些被上面的while循环弹出了,有些是最大值,只能因为窗口的移动而弹出
                q.popleft()
            if i >= k - 1:  # 开始队列为空,必须等到队列塞到窗口大小才开始求最大值
                ans.append(q[0])
        return [nums[x] for x in ans]  # 存储的是下标

    # 方法二:堆
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans





