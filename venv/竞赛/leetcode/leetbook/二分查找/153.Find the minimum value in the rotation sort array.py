# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/18 10:38'

import time
from typing import List


class Solution:
    # 方法一:二分查找--变形,我们需要明确最小值会在分割后的哪个范围里,然后不断缩小范围直至不能再缩小,此时即为最小值
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
