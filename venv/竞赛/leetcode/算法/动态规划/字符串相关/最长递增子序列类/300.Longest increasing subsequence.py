# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/28 13:18'
from typing import List


class Solution:
    # 方法一:动态规划
    # dp[i]表示以nums[i]结尾的最长递增子序列长度
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):  # 尝试在所有的递增子序列中选择最长的进行增长
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 并不是仅比上一个多1,而是比之前最长的递增子序列+1
        return max(dp)

    # 方法二:贪心算法
    # 题目要找最长递增子序列,要子序列最长,即序列中的各个数之间的间距应尽可能的小,这样才能在有限的区间(序列的上下限)内塞入更多的数字
    def lengthOfLIS2(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
