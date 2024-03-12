# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 20:31'

import time
from typing import List


class Solution:
    # 方法一:枚举
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                ans += sum(arr[j:j + i])
        return ans

    # 方法二:前缀和
    def sumOddLengthSubarrays2(self, arr: List[int]) -> int:
        sum_up = 0
        n = len(arr)
        prefixSums = [0] * (n + 1)
        for i, v in enumerate(arr):
            prefixSums[i + 1] = prefixSums[i] + v
        for start in range(n):
            length = 1
            while start + length <= n:
                end = start + length - 1
                sum_up += prefixSums[end + 1] - prefixSums[start]
                length += 2
        return sum_up


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
