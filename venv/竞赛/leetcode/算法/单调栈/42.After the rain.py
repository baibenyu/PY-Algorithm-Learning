# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/3 15:21'
from typing import List


class Solution:
    # 方法一:动态规划
    # 每个下标位置能接的雨水等于=左右最高的边界中较小的那一个-本身的高度
    # 换言之,我们需要知道每个位置的左右高度最大值,需提前存储
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):  # 左边各下标最大
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):  # 右边各下标最大
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

    # 方法二:单调栈
    # 基于方法一得到的每个位置的雨水存量公式可知,每个能储存雨水的位置必然有两边大于它高度的柱子,即凹陷,换言之每个储水位置都是单调递减序列的最后一个元素
    def trap2(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans

    # 方法三:双指针
    # 同样根据雨水储量公式,可知实际储水量取决于两面边界中较矮的边界
    def trap3(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:  # 而没找到之前,对于所有的左指针来说,它的左边界相对于右指针的右边界来说是较矮的边界(或者说从整个数组来看存在右边界高于此时的左边界)
                ans += leftMax - height[left]
                left += 1
            else:  # 左指针移动直至找到左边界高于右边界为止,即此时证明了对于右指针来说,它的右边界是较矮的边界
                ans += rightMax - height[right]
                right -= 1

        return ans
