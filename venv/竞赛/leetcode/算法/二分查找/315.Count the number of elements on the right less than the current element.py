# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 15:17'

import time
from bisect import bisect, bisect_left
from typing import List


class Solution:
    # 方法一:二分+排序数组
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sl = []  # 反向遍历的数字的有序数组

        for i in range(n - 1, -1, -1):  # 反向遍历
            pos = bisect.bisect_left(sl, nums[i])  # 处于有序数组的下标,即原数组右边比当前值小的元素个数
            res[i] = pos  # 记入答案
            sl.insert(pos, nums[i])  # 将当前值加入有序数组中

        return res


# 方法二:树状数组/线段树
# 暂未理解和学习,等待!!!!!!!!!!!!!
class Solution:
    max_len = 10000
    c = []
    buckets = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.c = [0 for _ in range(len(nums) + 5)]
        counts = [0 for _ in range(len(nums))]
        nums = self.discretization(nums)
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            counts[i] = self.query(num - 1)
            self.updateC(num)
        return counts

    def updateC(self, pos):
        while pos < len(self.c):
            self.c[pos] += 1
            pos += self.lowbit(pos)

    def lowbit(self, x):
        """获取更新范围"""
        return x & (-x)

    def query(self, pos):
        """查询前缀和"""
        val = 0
        while pos > 0:
            val += self.c[pos]
            pos -= self.lowbit(pos)
        return val

    def getMappingList(self, nums):
        """列表去重排序"""
        return list(sorted(set(nums)))

    def discretization(self, nums):
        """将nums进行离散化变换"""
        mapping = self.getMappingList(nums)
        return [bisect_left(mapping, num) + 1 for num in nums]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
