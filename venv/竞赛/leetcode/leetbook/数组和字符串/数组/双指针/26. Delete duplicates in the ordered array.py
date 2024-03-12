# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 16:47'

import time
from typing import List


class Solution:
    # 方法一:双指针--升序排序所以一旦不同说明遇到新的元素
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
