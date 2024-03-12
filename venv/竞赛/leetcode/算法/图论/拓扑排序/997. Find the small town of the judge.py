# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 18:19'

import time
from typing import List


class Solution:
    # 方法一:转换为图,然后统计入度和出度,入度为n-1,出度为0的即为法官
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        from collections import Counter
        inDegrees = Counter(y for _, y in trust)
        outDegrees = Counter(x for x, _ in trust)
        return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
