# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 18:24'

import time
from typing import List


class Solution:
    # 方法一:找到入度为0的点
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        endSet = set(y for x, y in edges)
        ans = [i for i in range(n) if i not in endSet]
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
