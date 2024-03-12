# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 15:50'

import time


class Solution(object):
    # 方法一:DP
    # dp表示每一行每个位置能取到的最小花费,从倒数第二行开始依次向上推
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0, i - 1): min(len(row), i + 2)])  # 避免超出边界
        return min(A[0])


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
