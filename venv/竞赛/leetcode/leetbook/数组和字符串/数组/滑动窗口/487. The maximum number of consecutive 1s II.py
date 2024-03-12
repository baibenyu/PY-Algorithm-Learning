# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 16:57'

import time
from typing import List


class Solution:
    # 方法一:记录0左右两边连续1的个数
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, prev, cnt = 0, 0, 0
        for num in nums:
            cnt += 1
            if num == 0:
                prev = cnt
                cnt = 0
            res = max(res, prev + cnt)
        return res

    # 方法二:滑动窗口--0的个数不能超过1个
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cnt0 = 0
        L = 0
        for R in range(n):  # 滑动窗口 进R
            if nums[R] == 0:
                cnt0 += 1

            while cnt0 > 1:  # 弹L
                if nums[L] == 0:
                    cnt0 -= 1
                L += 1

            res = max(res, R - L + 1)  # 更新res
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
