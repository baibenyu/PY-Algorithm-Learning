# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/3 16:22'
from typing import List


class Solution:
    # 方法一:排序+滑动窗口
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        count = 1
        max_c = 1
        length = len(nums)
        if not nums:
            return 0
        else:
            for i in range(1, length):
                if nums2[i] == nums2[i - 1] + 1:
                    count += 1
                    max_c = max(max_c, count)
                elif nums2[i] == nums2[i - 1]:  # 碰到相同的元素忽略
                    continue
                else:  # 重置窗口长度
                    count = 1
            return max_c

    # 方法二:哈希表
    # 哈希表基于当前数字的下一个数是否在
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
