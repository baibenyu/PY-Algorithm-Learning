# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/15 10:53'

import time
from bisect import bisect_left
from typing import List


class Solution:
    # 方法一:排序+二分查找--数对距离必定在最大值和最小值之间,
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)  # 统计原数组中的数对距离比当前距离小的有几个,直至找到k个为止
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key = count)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
