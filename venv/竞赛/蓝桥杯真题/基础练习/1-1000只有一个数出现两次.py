# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/10 21:46'
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        length = len(nums)
        for i in range(1, length):
            ans ^= i
        for num in nums:
            ans ^= num

        return ans
