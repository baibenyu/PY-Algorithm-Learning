# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 9:33'

import time
from typing import List


class Solution:
    # 方法一:双指针+数学--二次函数,一次函数性质
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # 抛物线判断开口。然后判断与对称轴的距离(直接计算结果也行)
        # 计算函数值
        def f(x: int) -> int:
            return a * (x ** 2) + b * x + c

        if not nums:
            return []
        n = len(nums)
        res = [0 for _ in range(n)]
        # 双指针，从外侧向中心“夹逼”的思想
        L, R = 0, n - 1
        # 抛物线开口向上，或者a==0一条直线（直线合并在哪种情况都行）
        if a >= 0:
            idx = n - 1  # 越外侧的越大
            while L <= R:
                if f(nums[L]) > f(nums[R]):
                    res[idx] = f(nums[L])
                    L += 1
                else:
                    res[idx] = f(nums[R])
                    R -= 1
                idx -= 1
        # 抛物线开口向下
        else:
            idx = 0  # 越外侧的越小
            while L <= R:
                if f(nums[L]) < f(nums[R]):
                    res[idx] = f(nums[L])
                    L += 1
                else:
                    res[idx] = f(nums[R])
                    R -= 1
                idx += 1
        # 返回结果
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
