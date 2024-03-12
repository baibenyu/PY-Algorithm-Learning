# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/10 17:49'

import time
from bisect import bisect
from typing import List


class Solution:
    # 方法一:前缀和+二分查找
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = [0]
        for num in nums:  # 将0变1,1变0
            P.append(P[-1] + (1 - num))

        ans = 0
        for right in range(n):
            left = bisect.bisect_left(P, P[right + 1] - k)  # 找一个区间内的1的个数(原0)不超过k
            ans = max(ans, right - left + 1)  # 计算区间长度,取最大

        return ans

    # 方法二:滑动窗口
    # 转换问题->找一个最长的子数组,数组内最多含k个0
    def longestOnes2(self, A, K):
        N = len(A)
        res = 0
        left, right = 0, 0
        zeros = 0
        while right < N:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
