# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/26 21:23'
from typing import List


class Solution:
    # 方法一:动态规划
    # 用dp[i]来表示nums[i]为结尾的子数组的最大和
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if not length:
            return 0
        else:
            dp = [float("-inf")] * length
            res = nums[0]
            dp[0] = nums[0]
            for i in range(1, length):  # 前一个结尾的最大和
                dp[i] = max(dp[i - 1] + nums[i],
                            nums[i])  # 注意!!!子数组是连续的,即必须保证num[i]要在dp[i]中,所以要在加和不加dp[i-1]之间选择,而不是在是否加nums[i]上选择
                res = max(res, dp[i])
            return res

    # 方法二:分治
    # 最大子数组和 = max(左边子数组和,右边子数组和,横款左右边界的中间子数组)
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和--从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)
