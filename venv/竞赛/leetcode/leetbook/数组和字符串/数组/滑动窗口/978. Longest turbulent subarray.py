# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/21 11:03'

import time

# 1.动态规划
# 未进行空间优化
from typing import List


class Solution(object):
    # 方法一:DP
    def maxTurbulenceSize(self, arr: List[int]):
        N = len(arr)
        up = [1] * N  # 以位置 i 结尾的,并且 arr[i - 1] < arr[i] 的最长湍流子数组长度
        down = [1] * N  # 以位置 i 结尾的,并且 arr[i - 1] > arr[i] 的最长湍流子数组长度
        res = 1
        for i in range(1, N):
            if arr[i - 1] < arr[i]:  # 湍流子数组的增长和降低是交替的
                up[i] = down[i - 1] + 1
                down[i] = 1
            elif arr[i - 1] > arr[i]:
                up[i] = 1
                down[i] = up[i - 1] + 1
            else:
                up[i] = 1
                down[i] = 1
            res = max(res, up[i], down[i])
        return res

    # 2.滑动窗口
    def maxTurbulenceSize2(self, arr: List[int]):
        n = len(arr)
        ret = 1
        left = right = 0

        while right < n - 1:
            if left == right:  # 特殊情况: 窗口长度为1
                if arr[left] == arr[left + 1]:  # 两指针相等时, 左右指针同时移动
                    left += 1

                right += 1  # 两指针不相等时, 只移动右指针
            else:  # 正常情况: 窗口长度不为1
                # 下面的两种情况下, 可以移动右指针扩大窗口
                if arr[right - 1] < arr[right] and arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] and arr[right] < arr[right + 1]:
                    right += 1
                else:  # 不满足时,[left,right+1]也无法构成湍流子数组,直接将left移到right
                    left = right

            ret = max(ret, right - left + 1)
        return ret


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
