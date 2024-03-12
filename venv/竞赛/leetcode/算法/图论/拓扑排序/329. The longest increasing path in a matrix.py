# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/24 17:07'
import collections
import time
from typing import List


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 方法一:记忆化搜索
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        import functools
        @functools.lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans

    # 方法二:拓扑排序
    class Solution:

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
            if not matrix:
                return 0

            rows, columns = len(matrix), len(matrix[0])
            outdegrees = [[0] * columns for _ in range(rows)]  # 邻接矩阵建图,统计出度为0的点,即矩阵中各条路径的终点
            queue = collections.deque()
            for i in range(rows):
                for j in range(columns):
                    for dx, dy in Solution.DIRS:
                        newRow, newColumn = i + dx, j + dy
                        if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                            outdegrees[i][j] += 1
                    if outdegrees[i][j] == 0:  # 记录终点
                        queue.append((i, j))

            ans = 0
            while queue:
                ans += 1
                size = len(queue)
                for _ in range(size):
                    row, column = queue.popleft()
                    for dx, dy in Solution.DIRS:
                        newRow, newColumn = row + dx, column + dy
                        if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][
                            column]:
                            outdegrees[newRow][newColumn] -= 1  # 顺着路径依次返回
                            if outdegrees[newRow][newColumn] == 0:
                                queue.append((newRow, newColumn))

            return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
