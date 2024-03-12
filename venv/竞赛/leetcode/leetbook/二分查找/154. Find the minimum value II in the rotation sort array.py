# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/15 9:15'

import time
from typing import List


class Solution:
    # 方法一:二分--根据当前值与最后值的大小关系确定最小值所处的范围,因为允许重复值所以当相等时无法定位,但可以去掉右边界,因为中间有一个与右边界相等的值
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
