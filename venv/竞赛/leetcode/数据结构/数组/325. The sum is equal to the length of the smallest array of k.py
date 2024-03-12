# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 16:24'

import time
from collections import defaultdict
from typing import List


class Solution:
    # 方法一:前缀和+哈希表
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum_idx = defaultdict(int)
        res = 0
        presum = 0
        presum_idx[0] = 0  # 前0个，和为0   也决定了必须用虚指
        for i in range(n):
            presum += nums[i]
            if presum not in presum_idx:  # 此处贪心,把所有前缀和出现的索引尽可能放在前面,即让长度尽可能长,所以只存储第一次出现下标
                presum_idx[presum] = i + 1
            if (presum - k) in presum_idx:
                res = max(res, i - presum_idx[presum - k] + 1)

        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
