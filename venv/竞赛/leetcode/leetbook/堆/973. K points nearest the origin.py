# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/21 20:54'
import heapq
import time
from typing import List


class Solution:
    # 方法一:排序,取前k个小值
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]

    # 方法二:堆
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)

        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))

        ans = [points[identity] for (_, identity) in q]
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
