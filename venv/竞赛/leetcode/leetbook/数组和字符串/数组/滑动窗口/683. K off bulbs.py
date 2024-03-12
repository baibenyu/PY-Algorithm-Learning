# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/25 9:27'

import time


class Solution(object):
    # 方法一:滑动窗口--重构条件数组,中间部分的亮起时间晚于两端
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, k + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + k + 1

        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
