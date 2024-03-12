# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/25 9:36'

import time
from collections import deque
from typing import List

import sortedcontainers


class Solution:
    # 方法一:滑动窗口--采用有序集合维护最小值和最大值O(1)地访问
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = sortedcontainers.SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1

        return ret

    # 方法二:滑动窗口--采用最小队列和最大队列维护最小值和最大值的O(1)访问
    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        queMax, queMin = deque(), deque()
        left = right = ret = 0

        while right < n:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()

            queMax.append(nums[right])
            queMin.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1

            ret = max(ret, right - left + 1)
            right += 1

        return ret


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
