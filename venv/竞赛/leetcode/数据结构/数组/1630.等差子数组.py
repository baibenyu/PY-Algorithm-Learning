# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/24 14:02'

import time
from typing import List


class Solution:
    # 方法一:排序+模拟
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m, n = len(l), len(nums)
        ans = []
        for i in range(m):
            temp = sorted(nums[l[i]:r[i] + 1])
            flag = True
            for j in range(1, len(temp) - 1):
                if temp[j] - temp[j - 1] != temp[j + 1] - temp[j]:
                    flag = False
                    break
            if flag:
                ans.append(True)
            else:
                ans.append(False)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
