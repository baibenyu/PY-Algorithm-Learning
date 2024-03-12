# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/23 8:04'

import time
from typing import List


class Solution:
    # 方法一:前缀和
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        prefix = [0]
        for i in range(len(calories)):
            prefix.append(prefix[-1] + calories[i])

        ans = 0
        for j in range(len(prefix) - k):
            if prefix[j + k] - prefix[j] > upper:
                ans += 1
            elif prefix[j + k] - prefix[j] < lower:
                ans -= 1

        return ans

    # 方法二:滑动窗口
    def dietPlanPerformance2(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        n = len(calories)
        window_sum = sum(calories[:k])  # 第一个窗口的和

        res = 0
        if window_sum < lower:
            res -= 1
        elif window_sum > upper:
            res += 1

        for R in range(k, n):  # 滑动窗口的右端（实指）
            window_sum -= calories[R - k]  # L端弹出
            window_sum += calories[R]  # R端进
            if window_sum < lower:
                res -= 1
            elif window_sum > upper:
                res += 1
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
