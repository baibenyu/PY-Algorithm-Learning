# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 14:43'
import heapq
import time
from typing import List


class Solution:
    # 方法一:二分+规律
    # 找第k小(大)的数都可以转换-->比k个数大(小),此处坐标处的数比左上角矩阵(i*j)的数都要大,比右下角矩阵((m-i)*(n-j))的数都要小
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

    # 方法二:归并
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]  # 第一列最小
        heapq.heapify(pq)

        for i in range(k - 1):  # 排除前k-1个小的元素,那么栈顶就是第k小
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
