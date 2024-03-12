# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/23 10:37'

import time
from typing import List


class Solution:
    # 方法一:排序
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums) + 1):
            if nums[-i] < i:
                if nums[-i] < i - 1:
                    return i - 1
                else:
                    return -1
        return len(nums)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
