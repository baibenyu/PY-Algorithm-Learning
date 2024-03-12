# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/23 10:47'
import heapq
import time
from random import random
from typing import List


class Solution:
    # 方法一:小根堆+二分
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r, pos = 0, n - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))

        heapq.heapify(power)
        ans = list()
        for i in range(k):
            ans.append(heapq.heappop(power)[1])
        return ans


# 方法二:二分+快速选择(只排序需要的那些数据)
class Helper:
    @staticmethod
    def partition(nums: List, l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    @staticmethod
    def randomized_partition(nums: List, l: int, r: int) -> int:
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return Helper.partition(nums, l, r)

    @staticmethod
    def randomized_selected(arr: List, l: int, r: int, k: int) -> None:
        pos = Helper.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            Helper.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            Helper.randomized_selected(arr, pos + 1, r, k - num)

    @staticmethod
    def getLeastNumbers(arr: List, k: int) -> List:
        Helper.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        power = list()
        for i in range(m):
            l, r, pos = 0, n - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            power.append((pos + 1, i))

        minimum = Helper.getLeastNumbers(power, k)[:k]
        minimum.sort()
        ans = [entry[1] for entry in minimum]
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
