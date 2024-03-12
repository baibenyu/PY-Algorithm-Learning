# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/23 17:21'

import time
from typing import List


class Solution:
    # 方法一:回溯+剪枝
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:  # 如果当前数字正在使用中直接跳过,避免重复
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:  # 如果当前数字在前一个位置已经使用过了
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
