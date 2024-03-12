# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/28 9:29'

import time
from random import random
from typing import List


class Solution:
    # 方法一:堆--大根堆解决前k小问题
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        import heapq
        maxheap = []
        for i, each in enumerate(arr):
            if i < k:
                heapq.heappush(maxheap, -each)
            else:
                if -each > maxheap[0]:
                    heapq.heapreplace(maxheap, -each)
        return [-a for a in maxheap]

    # 方法二:快速选择--快排改快选,部分排序,直至以k为分割
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
