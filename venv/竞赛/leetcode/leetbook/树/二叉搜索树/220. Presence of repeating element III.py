# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/18 8:48'

import time
import bisect
from typing import List
from sortedcontainers import SortedList


class Solution:
    # 方法一:桶排序
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getIdx(u):
            return ((u + 1) // size) - 1 if u < 0 else u // size

        map = {}
        size = t + 1
        for i, u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True
            # 检查相邻的桶
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            # 建立目标桶
            map[idx] = u
            # 维护个数为k
            if i >= k:
                map.pop(getIdx(nums[i - k]))

        return False

    # 方法二:滑动窗口+有序集合--将窗口内的元素变得有序,来缩短查找的时间
    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True
        return False


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
