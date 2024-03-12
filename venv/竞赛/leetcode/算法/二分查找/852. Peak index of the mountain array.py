# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 17:06'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -1
        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break
        return ans

    # 方法二:二分
    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
