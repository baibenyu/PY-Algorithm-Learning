# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/24 9:42'

import time
from typing import List


class Solution:
    # 方法一:双指针
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i = 0
        res = 0
        for j in range(n2):
            while i < n1 and nums1[i] > nums2[j]:
                i += 1
            if i < n1:
                res = max(res, j - i)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
