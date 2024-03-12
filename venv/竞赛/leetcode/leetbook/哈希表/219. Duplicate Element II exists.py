# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/12 15:44'

import time
from typing import List


class Solution:
    # 方法一:哈希表--只存储多个相同元素的最大下标
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

    # 方法二:滑动窗口
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
