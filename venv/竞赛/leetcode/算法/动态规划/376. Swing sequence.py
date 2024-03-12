# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 10:00'

import time
from typing import List


class Solution:
    # 方法一:DP
    # up表示前i个元素以上升趋势结尾的最长长度,down表示前i个元素以下降趋势结尾的最长长度
    # 如果当前元素大于前一个元素,说明应该接到下降序列中,反之同理
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(up[i - 1] + 1, down[i - 1])
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
