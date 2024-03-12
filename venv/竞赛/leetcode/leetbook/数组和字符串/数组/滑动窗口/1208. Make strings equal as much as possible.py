# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/21 9:49'

import time


class Solution:
    # 方法一:滑动窗口--窗口和不超过maxcost
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        costs = [0] * N
        for i in range(N):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        left, right = 0, 0
        res = 0
        sums = 0
        while right < N:
            sums += costs[right]
            while sums > maxCost:
                sums -= costs[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
