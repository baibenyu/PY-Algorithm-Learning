# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 9:19'

import time
from typing import List


class Solution:
    # 方法一:贪心
    # min每次都会丢掉一个较大值,为了减少损耗,我们每次取最小的两个值,保证了两数差距是最接近的,且损失最小
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
