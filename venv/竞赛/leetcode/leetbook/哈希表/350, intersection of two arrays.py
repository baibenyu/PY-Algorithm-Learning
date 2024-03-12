# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 10:14'

import time
from typing import List


class Solution:
    # 方法一:遍历一个数组,找是否存于另一个数组中,每找到一个相同的就要pop
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i, data in enumerate(nums1):
            if data in nums2:
                ans.append(nums2.pop(nums2.index(data)))
        return ans

    # 方法二:哈希表,统计各元素出现的次数,判断另一个数组中的元素是否在哈希表中,并且出现的次数不能大于哈希表,所以每次对哈希表-1
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import collections
        c = collections.Counter(nums1)
        ans = []
        for i, data in enumerate(nums2):
            if data in c and c[data] > 0:
                ans.append(data)
                c[data] -= 1
        return ans

    # 方法三:排序+双指针
    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        ans = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:  # 因为有序,让较小的指针动
                p2 += 1
            else:
                p1 += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
