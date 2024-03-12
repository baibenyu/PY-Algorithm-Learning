# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/24 21:59'
from typing import List


class Solution:
    # 方法一:删除所有0,并统计个数,然后在末尾添加相同个数的0
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        while 0 in nums:
            nums.remove(0)
        nums.extend([0] * (length - len(nums)))

    # 方法二:双指针
    # 当遇到非零元素时,左右指针共同移动,遇到0时,左指针停下来指向0,右指针继续移动
    # 左指针左边均为非0元素,右指针左边直到左指针处均为零,即每次将左指针的0与右指针的非0元素交换
    def moveZeroes2(self, nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1
