# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/22 20:54'

import time
from typing import List


class Solution:
    # 方法一:双指针
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        if nums[0] < 0 and nums[-1] > 0:  # 正负数均有
            left = 0
            while nums[left] < 0:  # 找到正负数的分界线
                left += 1
            right = left
            left -= 1
            while left >= 0 and right < length:
                if abs(nums[left]) <= abs(nums[right]):
                    ans.append(nums[left] ** 2)
                    left -= 1
                else:
                    ans.append(nums[right] ** 2)
                    right += 1
            while left >= 0:
                ans.append(nums[left] ** 2)
                left -= 1
            while right < length:
                ans.append(nums[right] ** 2)
                right += 1
        elif nums[0] < 0 and nums[-1] <= 0:  # 全员负数
            for i in range(length - 1, -1, -1):
                ans.append(nums[i] ** 2)
        else:  # 全员正数
            for i in range(length):
                ans.append(nums[i] ** 2)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
