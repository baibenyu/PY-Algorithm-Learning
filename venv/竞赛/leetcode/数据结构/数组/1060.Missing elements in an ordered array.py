# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 21:06'

import time
from typing import List


class Solution:
    # 方法一:线性扫描
    def missingElement(self, nums: List[int], k: int) -> int:
        start = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] != start:  # 不等时减少k的值
                k -= 1
            else:
                i += 1
            if k == 0:  # k等于0说明此时即为所求
                return start
            start += 1
        return start + k - 1

    # 方法二:二分查找
    def missingElement2(self, nums: List[int], k: int) -> int:
        # missing表示到该下标为止,总共缺失了几个数字
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        # 如果超出最大值,即拓展了边界,直接在最后的基础上增加即可
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        left, right = 0, n - 1
        # find left = right index such that
        # missing(left - 1) < k <= missing(left)
        while left != right:  # 找到k位于missing的哪个下标区间
            pivot = left + (right - left) // 2

            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot

                # kth missing number is larger than nums[left - 1]
        # and smaller than nums[left]
        return nums[left - 1] + k - missing(left - 1)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
