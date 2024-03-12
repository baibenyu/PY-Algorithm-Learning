# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/23 9:51'
import collections
import time
from typing import List


class Solution(object):
    # 方法一:滑动窗口--k个不同数字 = 最多k个不同数字-最多k-1个不同数字
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, A, K):
        N = len(A)
        left, right = 0, 0
        counter = collections.Counter()
        distinct = 0
        res = 0
        while right < N:
            if counter[A[right]] == 0:
                distinct += 1
            counter[A[right]] += 1
            while distinct > K:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    distinct -= 1
                left += 1
            res += right - left + 1
            right += 1
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
