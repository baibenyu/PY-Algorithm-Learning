# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 16:40'

import time
from typing import List


class Solution:
    # 方法一:贪心
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:  # 在可选范围内选最远
                maxPos = max(maxPos, i + nums[i])
                if i == end:  # 每当到了上一个最远的距离时才+1,换言之此时才确定了第二段范围内能跳到的最远距离
                    end = maxPos
                    step += 1
        return step


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
