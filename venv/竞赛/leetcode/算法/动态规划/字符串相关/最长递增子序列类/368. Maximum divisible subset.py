# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 10:28'

import time
from typing import List

"""
根据整除关系具有传递性，即如果ab，并且blc，那么ac，可知:
如果整数α是整除子集S1的最小整数b的约数(即ab)，那么可以将α添加到S1中得到一个更大的整除子集;
如果整数c是整除子集S2的最大整数d的倍数(即dc)，那么可以将c添加到S中得到一个更大的整除子集。
"""


class Solution:
    # 方法一:DP
    # 利用约数和倍数的可传递性
    # f[i]表示以nums[i]结尾的最长长度,g[j]表示取到当前长度的前驱结点
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        f, g = [0] * n, [0] * n
        for i in range(n):
            # 至少包含自身一个数，因此起始长度为 1，由自身转移而来
            length, prev = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    # 如果能接在更长的序列后面，则更新「最大长度」&「从何转移而来」
                    if f[j] + 1 > length:
                        length = f[j] + 1
                        prev = j
            # 记录「最终长度」&「从何转移而来」
            f[i] = length
            g[i] = prev

        # 遍历所有的 f[i]，取得「最大长度」和「对应下标」
        max_len = idx = -1
        for i in range(n):
            if f[i] > max_len:
                idx = i
                max_len = f[i]

        # 使用 g[] 数组回溯出具体方案
        ans = []
        while len(ans) < max_len:
            ans.append(nums[idx])
            idx = g[idx]
        ans.reverse()
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
