# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/21 9:29'

import time
from typing import List


class Solution:
    # 方法一:滑动窗口
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 哈希集合，记录每个数字是否出现过
        occ = set()
        n = len(nums)
        # 右指针，初始值为 -1，相当于我们在数组的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        cur = 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(nums[i - 1])  # 移除到无重复字符为止
                cur -= nums[i-1]
            while rk + 1 < n and nums[rk + 1] not in occ:  # 移动直到下一个数字是重复字符为止
                # 不断地移动右指针
                occ.add(nums[rk + 1])
                cur += nums[rk + 1]
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复子数组
            ans = max(ans, cur)
        return ans

if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
