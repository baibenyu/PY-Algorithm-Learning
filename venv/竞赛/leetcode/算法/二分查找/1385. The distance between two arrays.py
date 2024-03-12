# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 18:29'

import time


class Solution:
    # 方法一:模拟
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                cnt += 1
        return cnt

    # 方法二:二分
    def findTheDistanceValue2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for x in arr1:
            p = bisect.bisect_left(arr2, x)
            if p == len(arr2) or abs(x - arr2[p]) > d: # 超出范围则无需判断 or 第一个就超过d
                if p == 0 or abs(x - arr2[p - 1]) > d: # 同理 or 最接近也超过d
                    cnt += 1
        return cnt

if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
