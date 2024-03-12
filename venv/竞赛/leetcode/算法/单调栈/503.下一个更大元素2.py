# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/24 14:36'

import time
from typing import List


class Solution:
    # 方法一:单调栈+两次遍历
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        j = 0
        stack = []
        length = len(nums)
        ans = [-1 for _ in range(length)]
        for i in range(2 * length):
            if not stack or nums[j] <= nums[stack[-1]]:
                stack.append(j)
                j = (j + 1) % length
            else:
                while stack and nums[j] > nums[stack[-1]]:
                    ans[stack.pop()] = nums[j]
                stack.append(j)
                j = (j + 1) % length

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
