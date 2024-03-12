# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/5 15:54'

import time

grid = [[]]


def dfs(x, y):
    if grid[x][y] == 1:
        return
    grid[x][y] = 1
    for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= mx < m and 0 <= my < n:
            dfs(mx, my)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
