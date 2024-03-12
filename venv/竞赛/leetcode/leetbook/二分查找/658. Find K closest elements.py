# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/14 15:59'

import time
from typing import List


class Solution:
    # 方法一:堆+排序--涉及前k个,第k个问题均可以用堆
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        list1 = []
        for i in range(len(arr)):
            list1.append((abs(arr[i] - x), i))

        heapq.heapify(list1)
        ans = []
        for j in range(k):
            ans.append(arr[heapq.heappop(list1)[1]])
        ans.sort()
        return ans

    # 方法二:滑动窗口--题目的数组还已经排好序的,所以最近的k个数必然是连续的k个数
    def findClosestElements2(self, arr, k, x):
        minDelta = float('inf')
        delta = 0
        startIdx = 0
        for i in range(0, k):
            delta += abs(arr[i] - x)

        minDelta = min(delta, minDelta)
        for i in range(k, len(arr)):
            delta -= abs(arr[i - k] - x)
            delta += abs(arr[i] - x)
            if delta < minDelta:
                minDelta = delta
                startIdx = i - k + 1

        return arr[startIdx: startIdx + k]

    # 方法三:二分--确定下标,要最接近.所以当右端点更接近时要向右靠
    def findClosestElements3(self, arr, k, x):
        left = 0
        right = len(arr) - k - 1
        while left <= right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid - 1
        return arr[left: left + k]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
