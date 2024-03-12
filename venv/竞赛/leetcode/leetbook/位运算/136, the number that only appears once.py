# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/14 18:59'

import time
from typing import List


class Solution:
    # 方法一:位运算--异或
    # 两个相同的数异或等于零
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for each in nums:
            ans ^= each
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
