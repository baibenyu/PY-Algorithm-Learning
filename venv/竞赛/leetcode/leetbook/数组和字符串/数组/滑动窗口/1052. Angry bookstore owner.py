# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/20 8:31'

import time
from typing import List


class Solution:
    # 方法一:滑动窗口
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        good = []
        for i in range(len(customers)):  # 可以额外增加的满意人数
            if grumpy[i] == 0:
                good.append(0)
            else:
                good.append(customers[i])

        cur = sum(good[:minutes])
        maxnum = float("-inf")
        index = 0
        for j in range(minutes, len(good)):  # 滑动窗口求可增加满意最大值的开始下标
            if cur > maxnum:
                maxnum = cur
                index = j - minutes
            cur = cur - good[j - minutes] + good[j]
        if cur > maxnum:
            maxnum = cur
            index = len(good) - minutes

        ans = 0
        for k in range(len(good)):  # 求最大值
            if k < index or k >= index + minutes:
                ans += customers[k] if grumpy[k] != 1 else 0
            else:
                ans += customers[k]

        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
