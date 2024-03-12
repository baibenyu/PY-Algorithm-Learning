# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/18 19:23'

import time
from typing import List


class Solution:
    # 方法一:二分
    # 判断当前下标i缺失几个,即应该处于的下标-实际处于的下标
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k

        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) >> 1
            x = arr[mid] if mid < len(arr) else 10 ** 9
            if x - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1

        return k - (arr[l - 1] - (l - 1) - 1) + arr[l - 1]

    # 方法二:枚举
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        missCount = 0
        lastMiss = -1
        current = 1
        ptr = 0

        while missCount < k:
            if current == arr[ptr]:
                if ptr + 1 < len(arr):
                    ptr += 1
            else:
                missCount += 1
                lastMiss = current
            current += 1

        return lastMiss


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
