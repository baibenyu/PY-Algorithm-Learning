# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/19 16:11'

import time
from typing import List


class Solution:
    # 方法一:枚举
    # 题目等价于寻找一个下标i,其左边有小于它的值,右边有大于它的值
    # 更近一步降低要求,可以说只需要左边最小值小于它,右边最大值大于它,所以两次遍历建立每个位置左边最小值和右边最大值
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        leftMin = [0] * n
        leftMin[0] = nums[0]
        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i])

        rightMax = [0] * n
        rightMax[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])

        for i in range(1, n - 1):
            if leftMin[i - 1] < nums[i] < rightMax[i + 1]:
                return True
        return False

    # 方法二:贪心
    # 在三元组中的每个值都尽量小
    def increasingTriplet2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float('inf')
        for i in range(1, n):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
