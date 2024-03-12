# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/1 8:34'

import time
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断,因为如果是负数,那么此时数字对应的是原码下的十进制数,要转为补码对应下的十进制数
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
