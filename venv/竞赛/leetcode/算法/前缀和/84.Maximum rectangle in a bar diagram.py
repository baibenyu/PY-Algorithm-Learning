# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 10:36'
from typing import List


class Solution:
    # 方法一:单调栈
    # 首先,将所有可能矩形的高度按柱子来分类,每个柱子都希望自己的高度被保留,而尽可能拓展自己的宽度,高度是由经过的柱子中最矮的所决定,即每个柱子都应该在宽度内所有柱子中最矮
    # 换言之,在经过比自身矮的柱子时,意味着这是宽度的边界了,在前进就要降低高度，即我们只需要知道左右两边比自身矮的柱子的位置，而不需要高的柱子，因为高的柱子不限制此时的高度
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):  # 左边界
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:  # 当之前的柱子高度大于现在的高度,就出栈,因为它的高度不影响当前高度的最小值
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1  # 若左边所有柱子都比自己高,赋值为-1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):  # 右边界
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n  # 同上
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
