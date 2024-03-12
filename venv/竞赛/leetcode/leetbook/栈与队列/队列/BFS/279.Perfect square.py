# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 14:30'

import time
import math


class Solution:
    # 方法一:DFS+剪枝
    def numSquares(self, n: int) -> int:

        def backing(target: int, index: int, llimit: int, number: int, temp: int, max_square: int):
            nonlocal count
            if index == number:
                if temp == target:
                    count.append(number)
                return
            else:
                for i in range(llimit, max_square + 1):
                    temp += i ** 2
                    if temp > target:
                        temp -= i ** 2
                        break
                    backing(target, index + 1, i, number, temp, max_square)
                    temp -= i ** 2

        max_square = int(math.sqrt(n))
        count = list()
        for _ in range(1, n + 1):
            backing(n, 0, 0, _, 0, max_square)
            if count:
                return count[0]

    # 方法二:完全背包DP
    def numSquares2(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]

    # 方法三:BFS
    def numSquares3(self, n: int) -> int:
        from collections import deque
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    x = tmp - i ** 2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.appendleft(x)
                        visited.add(x)
        return step


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
