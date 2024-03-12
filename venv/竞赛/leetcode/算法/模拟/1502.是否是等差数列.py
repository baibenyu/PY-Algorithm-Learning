# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 10:49'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) < 3:
            return True
        else:
            tolerance = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != tolerance:
                    return False
            return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
