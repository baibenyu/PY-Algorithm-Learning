# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/18 10:54'

import time
from typing import List


class Solution:
    # 方法一:二分查找--变形
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
