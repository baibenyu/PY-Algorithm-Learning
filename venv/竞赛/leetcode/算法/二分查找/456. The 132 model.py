# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 16:24'

import time
from typing import List


class Solution:
    # 方法一:遍历 3
    def find132pattern(self, nums: List[int]) -> bool:
        import sortedcontainers  # 有序集合
        n = len(nums)
        if n < 3:
            return False

        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = sortedcontainers.SortedList(nums[2:])

        for j in range(1, n - 1):
            if left_min < nums[j]:
                index = right_all.bisect_right(left_min)  # 二分找比左侧最小值大一点的数
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])

        return False

    # 方法二:遍历 1
    def find132pattern2(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:  # 此处满足 1 < 3
                return True
            while candidate_k and nums[i] > candidate_k[-1]:  # 单调递减栈,使得max_k始终为3的可能值
                max_k = candidate_k.pop()
            if nums[i] > max_k:  # 此处满足 3 < 2
                candidate_k.append(nums[i])

        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
