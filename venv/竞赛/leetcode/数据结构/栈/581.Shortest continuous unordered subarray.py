# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/16 20:35'
from typing import List


class Solution:
    # 方法一:从头和尾找与升序排序后数组不同的位置,在用总长度减去相同部分的长度,剩下即为最短无序子数组长度
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        nums2.sort()
        length = len(nums)
        same = 0
        for i in range(length):
            if nums2[i] == nums[i]:
                same += 1
            else:
                break
        for i in range(length - 1, -1 + same, -1):
            if nums2[i] == nums[i]:
                same += 1
            else:
                break
        return length - same
