# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 20:30'
from typing import List


class Solution:
    # 方法一:出现几次就mod几
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

