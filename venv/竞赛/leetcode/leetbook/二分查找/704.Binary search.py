# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/21 17:10'

import time
from typing import List

start = time.clock()


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


end = time.clock()
print(end - start)
