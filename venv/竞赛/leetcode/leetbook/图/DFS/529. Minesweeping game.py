# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/5 10:36'

import time
from typing import List


class Solution:
    # 方法一:DFS
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def dfs(x, y):
            if newboard[x][y] == "M":
                newboard[x][y] = "X"
                return
            elif newboard[x][y] == "E":
                mine = 0
                for i, j in directions:
                    dx, dy = x + i, y + j
                    if 0 <= dx < m and 0 <= dy < n and newboard[dx][dy] == "M":
                        mine += 1
                if mine:
                    newboard[x][y] = f"{mine}"
                else:
                    newboard[x][y] = "B"
                    for i, j in directions:
                        dx, dy = x + i, y + j
                        if 0 <= dx < m and 0 <= dy < n:
                            dfs(dx, dy)

        directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        newboard = copy.deepcopy(board)
        m, n = len(newboard), len(newboard[0])
        dfs(click[0], click[1])

        return newboard


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
