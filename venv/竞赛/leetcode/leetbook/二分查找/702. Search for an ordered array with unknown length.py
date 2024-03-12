# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/14 17:10'

import time


class Solution:
    # 方法一:二分+扩右边界
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0

        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1

        # there is no target element
        return -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
