# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 9:46'

import time
from typing import List


class Solution:
    # 方法一:双指针--枚举山顶
    def longestMountain(self, arr: List[int]) -> int:
        if not arr:
            return 0

        n = len(arr)
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if arr[i - 1] < arr[i] else 0)

        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if arr[i + 1] < arr[i] else 0)

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans

    # 方法二:双指针--枚举山脚
    def longestMountain2(self, arr: List[int]) -> int:
        n = len(arr)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if arr[left] < arr[left + 1]:
                while right + 1 < n and arr[right] < arr[right + 1]:  # 上行部分
                    right += 1
                if right < n - 1 and arr[right] > arr[right + 1]:
                    while right + 1 < n and arr[right] > arr[right + 1]:  # 下行部分
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
