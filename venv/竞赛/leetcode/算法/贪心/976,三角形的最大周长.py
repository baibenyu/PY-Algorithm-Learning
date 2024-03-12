# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 9:05'

import time
from typing import List


class Solution:
    # 方法一:贪心+对边长排序
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        for i in range(length - 1, 1, -1):  # 若不满足无需尝试前面更小的边长,因为更不可能满足
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i - 1] + nums[i - 2] + nums[i]
        return 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
