# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 17:10'
import collections
import time
from typing import List


class Solution:
    # 方法一:BFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = {0}
        que = collections.deque([0])
        num = 0
        while que:
            x = que.popleft()
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    vis.add(it)
                    que.append(it)

        return num == n

    # 方法二:DFS
    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)

        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
