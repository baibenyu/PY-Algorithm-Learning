# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 9:19'

import time
from typing import List


class Solution:
    # 方法一:排序+双指针
    def func(self, nums: List[int], L: int, target: int) -> int:  # 两个数的和小于target
        res = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] + nums[R] < target:  # r减小也一直成立
                res += (R - L)
                L += 1
            else:
                R -= 1
        return res

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n - 2):  # 3个数的和，分解成2个数的和  先固定住一个变量，控制变量
            res += self.func(nums, i + 1, target - nums[i])
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
