# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/21 8:37'

import time


class Solution(object):
    # 方法一:滑动窗口
    def minOperations(self, nums, x):
        target = sum(nums) - x
        windowSum = 0
        N = len(nums)
        maxLen = -1
        left, right = 0, 0
        while right < len(nums):
            windowSum += nums[right]
            while left < N and windowSum > target:  # 坑，别忘i < N
                windowSum -= nums[left]
                left += 1

            if windowSum == target:
                maxLen = max(maxLen, right - left + 1)
            right += 1

        if maxLen == -1:
            return -1

        return N - maxLen


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
