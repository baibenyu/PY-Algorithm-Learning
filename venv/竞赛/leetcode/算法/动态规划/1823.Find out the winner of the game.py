# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/29 9:37'

import time


class Solution:
    # 方法一:模拟
    def findTheWinner(self, n: int, k: int) -> int:
        ans = [i for i in range(n)]
        j = 0
        while len(ans) > 1:
            j = (j + k - 1) % len(ans)
            ans.pop(j)
        return ans[0] + 1

    # 方法二:DP
    # 实际上就是求第n个被踢出的人
    def findTheWinner2(self, n, k):
        if n == 1:
            return 1
        val = 0
        for i in range(2, n + 1):  # 倒数第i个被踢出的人的下标
            cur = (val + k) % i
            val = cur
        return val + 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
