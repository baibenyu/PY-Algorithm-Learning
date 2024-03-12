# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/14 19:38'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        else:
            l, r = 0, 1
            while r < n and nums[r] == nums[l]:  # 向后推直至不相等
                l += 1
                r += 1
            if r < n and nums[r] > nums[l]:  # 判断是递增还是递减
                while r < n:
                    if nums[r] >= nums[l]:
                        l += 1
                        r += 1
                    else:
                        return False
            elif r < n and nums[r] < nums[l]:
                while r < n:
                    if nums[r] <= nums[l]:
                        l += 1
                        r += 1
                    else:
                        return False
            return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
