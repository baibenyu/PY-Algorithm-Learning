# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/17 10:09'
from typing import List


class Solution:
    # 方法一:二分--利用大于数和小于数的数量,来确定数的位置
    # 对于连续有序不重复数组进行二分查找,并统计各数在给定数组中有多少个数小于等于它,若大于它本身,说明给定数组中小于等于它的数中可能有重复出现
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left

    # 方法二:快慢指针
    # 因为存在重复的数且n>0,所以用数组建图必然存在环
    def findDuplicate2(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while 1:  # 让慢指针停在相遇点
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        find = 0
        while 1:  # 从头出发,让指针相遇,此时即为重复点
            find = nums[find]
            slow = nums[slow]
            if find == slow:
                return find
