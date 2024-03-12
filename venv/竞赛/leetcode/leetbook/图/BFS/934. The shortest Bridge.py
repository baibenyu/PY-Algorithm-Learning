# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 15:56'
import collections
import time


class Solution:
    # 方法一:多源BFS,只是需要先通过DFS确定各个源在哪
    def shortestBridge(self, nums):
        def dfs(i, j):  # 把找到的一个岛染成2，同时把找个岛的所有坐标放到队列q
            if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]) or nums[i][j] == 0 or nums[i][j] == 2:
                return
            if nums[i][j] == 1:
                nums[i][j] = 2
                q.append((i, j))
                for x, y in dirs:
                    newi, newj = x + i, y + j
                    dfs(newi, newj)

        def bfs(i, j):  # 从找到的岛开始扩展，每扩展一层，steps+1
            steps = 0
            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()
                    for x, y in dirs:
                        newi, newj = x + i, y + j
                        if newi < 0 or newi >= len(nums) or newj < 0 or newj >= len(nums[0]) or nums[newi][newj] == 2:
                            continue
                        if nums[newi][newj] == 1:
                            return steps
                        nums[newi][newj] = 2
                        q.append((newi, newj))
                steps += 1

        # main
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = collections.deque()
        for i, row in enumerate(nums):
            for j, ele in enumerate(row):
                if ele == 1:
                    dfs(i, j)
                    return bfs(i, j)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
