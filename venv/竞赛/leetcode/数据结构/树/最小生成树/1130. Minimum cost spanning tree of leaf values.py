# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 20:00'

import time
from typing import List


class Solution:
    # 方法一:单调栈+最小生成树
    def mctFromLeafValues(self, A: List[int]) -> int:
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
