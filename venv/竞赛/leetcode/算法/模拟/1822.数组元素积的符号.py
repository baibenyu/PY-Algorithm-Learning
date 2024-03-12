# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 10:35'

import time
from typing import List


class Solution:
    # 方法一:若数组含0则为0,接下来取决于负数的个数,若为奇数个负数则返回-1,否则返回1
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            ans = 1
            for i in range(len(nums)):
                if nums[i] < 0:
                    ans = -ans
            return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
