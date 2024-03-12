# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/10 16:20'
import collections
import time
from typing import List


class Solution:
    # 方法一:分组求值+哈希表
    # 本题之所以可以只求A和B得出的和,是因为四元组的各个数实际上是确定的,无论哪两个列表组合,仅待匹配的数字可能不同,但数字的个数是一样多的
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
