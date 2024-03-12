# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/18 11:18'

import time
from typing import List


class Solution:
    # 方法一:双指针--理清两个指针的含义与功能
    def removeDuplicates(self, nums: List[int]) -> int:
        def solve(k):
            u = 0  # u左边的元素都符合条件,u下标对应的数字就是第一个多余的重复元素
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            return u

        return solve(2)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
