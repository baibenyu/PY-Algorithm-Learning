# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/23 17:16'

import time
from typing import List


class Solution:
    # 方法一：回溯
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放符合条件结果的集合
        path = []  # 用来存放符合条件结果

        def backtrack(nums, startIndex):
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:  # 我们要对同一树层使用过的元素进行跳过
                    continue
                path.append(nums[i])
                backtrack(nums, i + 1)  # 递归
                path.pop()  # 回溯

        nums = sorted(nums)  # 去重需要排序
        backtrack(nums, 0)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
