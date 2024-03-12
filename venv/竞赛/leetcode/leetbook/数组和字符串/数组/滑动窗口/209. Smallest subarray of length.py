# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/20 16:25'

import time
from bisect import bisect
from typing import List


class Solution:
    # 方法一:滑动窗口
    # 扩展直至刚刚大于target,然后左边收缩取长度
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 1
        cur = nums[0]
        ans = float("inf")
        while left < right:
            while right < len(nums) and cur < target:
                cur += nums[right]
                right += 1
            if cur >= target:
                ans = min(right - left, ans)
            cur -= nums[left]
            left += 1
        if ans == float("inf"):
            return 0
        else:
            return ans

    # 方法二:前缀和+二分查找
    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)  # 在数据中找到仅比s大的下标
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
