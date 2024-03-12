# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 15:22'

import time
import math
from typing import List


class Solution:
    # 方法一:裴蜀定理--对于最大公约数为1的一连串数字,这些数字互质
    def isGoodArray(self, nums: List[int]) -> bool:
        ans = nums[0]
        for num in nums:
            ans = math.gcd(ans, num)
        return ans == 1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
