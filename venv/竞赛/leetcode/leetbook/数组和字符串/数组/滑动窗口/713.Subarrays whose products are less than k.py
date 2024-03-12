# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/20 15:53'
import math
import time
from bisect import bisect


class Solution(object):
    # 方法一：滑动窗口
    # 统计个数的规律
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1  # 核心！！！
        return ans

    # 方法二：二分查找
    # 对于每一个i位置找到第一个乘积大于k的位置
    def numSubarrayProductLessThanK2(self, nums, k):
        if k == 0:
            return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i + 1)
            ans += j - i - 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
