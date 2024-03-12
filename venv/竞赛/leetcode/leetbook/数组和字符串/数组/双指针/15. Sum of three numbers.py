# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/28 20:30'
from typing import List


class Solution:
    # 方法一:双指针--即两个索引值有同步关系,一个索引值改变能引起另一个索引值的变化
    # 本体难点在于如何在遍历时去重
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):  # 固定a的值
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:  # 去除重复元素
                continue
            L = i + 1
            R = n - 1
            while L < R:  # 用双指针同时遍历a后面的序列,凑出0
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:  # 去除重复元素
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
        return res
