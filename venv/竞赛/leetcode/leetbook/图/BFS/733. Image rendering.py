# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 19:33'

import time
from typing import List


class Solution:
    # 方法一:DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def dfs(x, y):
            nonlocal ans
            for each in directions:
                dx = x + each[0]
                dy = y + each[1]
                if 0 <= dx < m and 0 <= dy < n and ans[dx][dy] == target and isvis[dx][dy] == 0:
                    ans[dx][dy] = newColor
                    isvis[dx][dy] = 1
                    dfs(dx, dy)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        image[sr][sc] = newColor
        isvis = [[0 for _ in range(n)] for _ in range(m)]  # 防止重复搜索
        ans = image.copy()
        dfs(sr, sc)
        return ans

    # 方法二:BFS
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        import collections
        q = collections.deque([(sr, sc)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        isvis = [[0 for _ in range(n)] for _ in range(m)]
        ans = image.copy()
        while q:
            temp = q.popleft()
            if image[temp[0]][temp[1]] == target and isvis[temp[0]][temp[1]] == 0:
                ans[temp[0]][temp[1]] = newColor
                isvis[temp[0]][temp[1]] = 1
                for each in directions:
                    dx = temp[0] + each[0]
                    dy = temp[1] + each[1]
                    if 0 <= dx < m and 0 <= dy < n and ans[dx][dy] == target and isvis[dx][dy] == 0:
                        q.append((dx, dy))

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
