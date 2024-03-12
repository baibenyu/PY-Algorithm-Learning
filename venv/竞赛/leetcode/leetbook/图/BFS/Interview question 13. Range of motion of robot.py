# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/8 6:54'

import time


class Solution:
    # 方法一:BFS--遍历过程中判断是否超过k
    def movingCount(self, m: int, n: int, k: int) -> int:
        import collections
        q = collections.deque([(0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = {(0, 0)}
        ans = 0
        while q:
            row, col = q.popleft()
            ans += 1
            for x, y in directions:
                dx, dy = x + row, y + col
                if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited:
                    tempx, tempy = dx, dy
                    sumup = 0
                    while tempx:
                        sumup += tempx % 10
                        tempx //= 10
                    while tempy:
                        sumup += tempy % 10
                        tempy //= 10
                    if sumup <= k:
                        q.append((dx, dy))
                        visited.add((dx, dy))
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
