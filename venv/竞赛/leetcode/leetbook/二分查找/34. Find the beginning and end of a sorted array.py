# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/2 21:10'
from typing import List


class Solution:
    # 方法一:先二分查找,找到目标后向左和向右移动直至不是为止
    # 优化->找target-1和target+1的位置再减一即为左右边界
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        left, right = 0, length - 1
        if target in nums:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    l, r = mid, mid
                    while l > 0 and nums[l - 1] == target:
                        l -= 1
                    while r < length - 1 and nums[r + 1] == target:
                        r += 1
                    return [l, r]
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            return [-1, -1]

    # 方法二:找小于target和大于target
    class Solution:

        # 寻找左边界
        def leftMargin(self, nums: List[int], target: int):

            low, high = 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                # 如果 nums[mid] = target，继续向左寻找左边界
                if nums[mid] == target:
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            if nums[low] == target:
                return low
            # 如果左边界的值不等于 target
            else:
                return -1

        # 寻找右边界
        def rightMargin(self, nums: List[int], target: int):

            low, high = 0, len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                # 如果 nums[mid] = traget，继续向右寻找右边界
                if nums[mid] == target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            if nums[high] == target:
                return high
            # 如果右边界的值不等于 target
            else:
                return -1

        def searchRange(self, nums: List[int], target: int) -> List[int]:

            if len(nums) == 0 or nums[0] > target or nums[-1] < target:
                return [-1, -1]

            lm = self.leftMargin(nums, target)
            rm = self.rightMargin(nums, target)

            return [lm, rm]
