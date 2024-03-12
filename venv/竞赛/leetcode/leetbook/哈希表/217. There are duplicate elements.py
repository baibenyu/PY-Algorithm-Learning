# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/21 17:33'

import time
from typing import List

start = time.clock()


class Solution:
    # 方法一:集合
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


end = time.clock()
print(end - start)
