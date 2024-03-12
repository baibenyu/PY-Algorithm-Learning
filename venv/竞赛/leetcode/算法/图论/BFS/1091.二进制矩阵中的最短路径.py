# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/29 15:14'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:BFS
    # 本题只适用BFS
    # BFS适用于遍历所有情况找最值,无论如何都要遍历所有
    # DFS适用于遍历所有情况找存在,只要存在即可退出,无需真正遍历所有
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        length = len(grid)
        if length == 1:
            return 1
        que = deque()
        visited = {}
        que.appendleft((0, 0))
        visited[(0, 0)] = True
        start = 1
        while que:
            for _ in range(len(que)):
                ind, con = que.pop()
                for pos_h, pos_v in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    new_ind = ind + pos_h
                    new_con = con + pos_v
                    if 0 <= new_ind < length and 0 <= new_con < length and grid[new_ind][new_con] == 0 and not visited.get((new_ind, new_con)):
                        if new_ind == length - 1 and new_con == length - 1:
                            return start + 1
                        que.appendleft((new_ind, new_con))
                        visited[(new_ind, new_con)] = True
            start += 1
        return -1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
