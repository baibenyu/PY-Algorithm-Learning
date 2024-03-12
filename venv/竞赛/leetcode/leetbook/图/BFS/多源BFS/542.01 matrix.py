# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/29 16:35'
import collections
import time
from typing import List


class Solution:
    # 方法一:BFS
    # 对于多源的最短路径,可以视为有一个超级源头,由这个超级源头到各源头
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)  # 所有的源都视为由超级源头遍历后得到

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return dist


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
