# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/22 20:12'

import time
from typing import List


# 方法三:先合并两数组然后排序
class Solution:
    # 方法一:双指针
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = 0, 0
        temp = nums1.copy()
        i = 0
        while p1 < m and p2 < n:
            if temp[p1] <= nums2[p2]:
                nums1[i] = temp[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
            i += 1
        while p1 < m:  # 哪个数组还没复制完,继续复制
            nums1[i] = temp[p1]
            p1 += 1
            i += 1
        while p2 < n:
            nums1[i] = nums2[p2]
            p2 += 1
            i += 1

    # 方法二:逆向双指针--将较大值放置在nums1后面的空位
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
