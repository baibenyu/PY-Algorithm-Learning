# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/7 14:42'

import time
from typing import List


class Solution:
    # 方法一:二分查找
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def check(x):  # 测试当前自己的甜度能否分割出k+1块满足条件的
            s = 0  # 当前组的甜度和
            count = 0  # 分割出的组数
            for num in sweetness:
                s += num  # 因为题目要求连续的小块,所以s可以直接加
                if s >= x:
                    count += 1
                    s = 0
            return count >= K + 1

        l, r = 0, sum(sweetness) // (K + 1)  # 切割k次得k+1块,求甜度总和除以k+1得出自己能得到的理论甜度上限
        while l < r:  # 因为只需要知道极限状态下的甜度上限,而不需要一直成立,所以可用二分法逼近真正的上限
            mid = l + (r - l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
