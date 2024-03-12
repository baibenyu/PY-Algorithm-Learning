# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 21:32'
from functools import cache
from typing import List


class Solution:
    # 方法一:DFS+缓存
    def findTargetSumWays(self, nums: List[int], V: int) -> int:
        @cache
        def dfs(target, ind):
            if ind == len(nums):
                return 1 if target == 0 else 0
            res = 0
            res += dfs(target - nums[ind], ind + 1)
            res += dfs(target + nums[ind], ind + 1)
            return res

        return dfs(V, 0)


