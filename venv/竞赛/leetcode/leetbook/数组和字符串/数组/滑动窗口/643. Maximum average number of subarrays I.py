# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/20 7:47'

import time
from typing import List


class Solution:
    # 方法一:前缀和
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])

        ans = float("-inf")
        for j in range(k, len(prefix)):
            ans = max((prefix[j] - prefix[j - k]) / k, ans)
        return ans

    # 方法二:滑动窗口
    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
