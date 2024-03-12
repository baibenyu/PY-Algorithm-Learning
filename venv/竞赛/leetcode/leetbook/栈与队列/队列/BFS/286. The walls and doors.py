# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/12 15:57'

import time
from collections import deque
from typing import List


class Solution:
    # 方法一:超级源头--多源BFS最短路
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return rooms
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        m = len(rooms)
        n = len(rooms[0])
        # 先把有门的地方都放进来，定义有门的地方path距离是0
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        # 多源同时进行BFS
        while q:
            r, c, path = q.popleft()
            for i in range(4):
                newr, newc = r + dr[i], c + dc[i]
                if 0 <= newr < m and 0 <= newc < n and 2147483647 == rooms[newr][newc]:
                    rooms[newr][newc] = path + 1
                    q.append((newr, newc, path + 1))


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
