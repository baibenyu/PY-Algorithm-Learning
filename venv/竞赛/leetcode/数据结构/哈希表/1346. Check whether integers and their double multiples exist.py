# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/23 10:55'
import collections
import time
from typing import List


class Solution:
    # 方法一:哈希表
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        for n in arr:
            if n != 0 and counter[2 * n] >= 1:
                return True
            if n == 0 and counter[2 * n] >= 2:
                return True
        return False

    # 方法二:排序+双指针
    def checkIfExist2(self, arr: List[int]) -> bool:
        arr.sort()
        q = 0
        for p in range(len(arr)):
            while q < len(arr) and arr[p] * 2 > arr[q]:
                q += 1
            if q != len(arr) and p != q and arr[p] * 2 == arr[q]:
                return True
        q = len(arr) - 1
        for p in range(len(arr) - 1, -1, -1):
            while q > -1 and arr[p] * 2 < arr[q]:
                q -= 1
            if q != -1 and p != q and arr[p] * 2 == arr[q]:
                return True
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
