# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 16:54'

import time
from typing import List


class Solution:
    # 方法一:滑动窗口
    def minSwaps(self, data: List[int]) -> int:
        n = data.count(1)
        cur = sum(data[:n])
        res = n - cur
        for j in range(n, len(data)):
            if data[j]:
                cur += 1
            if data[j - n]:
                cur -= 1
            res = min(res, n - cur)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
