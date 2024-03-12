# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/20 11:02'
from typing import List


class Solution:
    # 方法一:双指针
    # 每一次得出的盛水值,是包括矮的那个指针的最大盛水值,也即无论如何向两边界中心移动另一个较大的指针,这个最大值都不会改变了,
    # 也即每一次移动指针都意味着包含矮边界的最大盛水值被确定,然后遍历包含每个边界的最大盛水值,取最大的那个就是整体最大值
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

