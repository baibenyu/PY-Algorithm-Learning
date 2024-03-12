# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/27 21:32'
from typing import List


class Solution:
    # 方法一:动态规划--01背包
    # 设所有正数和为a,负数(符号取-)和绝对值为b,所有元素和为sum
    # a+b = sum,target = a-b = sum-2b -> b = (sum-target)/2 因为b是正整数,所以target<sum,且sum-target为偶数
    # 本体关键点在于将问题转换为有几种方式可以得到b,即01背包的求方案个数问题,因为sum是固定的,target也是固定的,即b是固定的
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumValue = sum(nums)
        if target > sumValue or (sumValue + target) % 2 == 1 or target < -sumValue:  # 超出上下限
            return 0
        bagSize = (sumValue + target) // 2  # 此处求a
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):  # 遍历各种情况,即nums中的各个数字
            for j in range(bagSize, nums[i] - 1, -1):  # 对于所有的背包容量都要求各种情况,因为目标背包容量依赖于前面的背包容量
                dp[j] += dp[j - nums[i]]  # 有len(nums)种情况可以得到j,j的方案总数等于所有情况的和
        return dp[bagSize]


s = Solution()
s.findTargetSumWays([1, 1, 1, 1, 1], 3)
