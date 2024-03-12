# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 19:35'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        maxnum = max(nums2)
        ans = []
        for each in nums1:
            if each == maxnum:
                ans.append(-1)
                continue
            temp = nums2.index(each)
            flag = False
            for i in range(temp, len(nums2)):
                if nums2[i] > each:
                    ans.append(nums2[i])
                    flag = True
                    break
            if not flag:
                ans.append(-1)
        return ans

    # 方法二:单调栈+哈希表
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        check = dict()
        ans = []
        for each in nums2:
            if not stack or each < stack[-1]:
                stack.append(each)
            else:
                while stack and each > stack[-1]:  # 碰到大的就一直出栈
                    temp = stack.pop()
                    check[temp] = each
                stack.append(each)
        while stack:
            check[stack.pop()] = -1
        for each in nums1:
            ans.append(check.get(each))
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
