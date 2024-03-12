# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/9 20:20'

import time
from typing import List


class Solution:
    # 方法一:模拟--先将shift的移动统计完成,左右抵消后再最后移动一次
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n, m, cur = len(shift), len(s), 0
        for i in range(n):
            if shift[i][0] == 0:
                cur += shift[i][1]
            else:
                cur += m - shift[i][1]
        cur %= m
        return s[cur:] + s[:cur]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
