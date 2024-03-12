# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/1 8:05'

import time
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        for data in arr:
            ans.append((data, bin(data).count("1")))
        ans = sorted(ans, key = lambda x: (x[1], x[0]))
        return [x[0] for x in ans]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
