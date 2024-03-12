# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/17 8:57'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        up, down, left, right = 0, n - 1, 0, n - 1
        i, j = 0, 1
        while left <= right and up <= down:
            if i == 0:
                cur = left
                while cur <= right:
                    ans[up][cur] = j
                    j += 1
                    cur += 1
                up += 1
            elif i == 1:
                cur = up
                while cur <= down:
                    ans[cur][right] = j
                    j += 1
                    cur += 1
                right -= 1
            elif i == 2:
                cur = right
                while cur >= left:
                    ans[down][cur] = j
                    j += 1
                    cur -= 1
                down -= 1
            else:
                cur = down
                while cur >= up:
                    ans[cur][left] = j
                    j += 1
                    cur -= 1
                left += 1
            i = (i + 1) % 4
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
