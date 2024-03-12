# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/12 9:04'
import collections
import time
from typing import List


class Solution:
    # 方法一:哈希表
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        m = collections.Counter(nums1)
        intersection = list()
        for num in nums2:
            if m.get(num, 0) > 0 and num not in intersection:
                intersection.append(num)

        return intersection


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
