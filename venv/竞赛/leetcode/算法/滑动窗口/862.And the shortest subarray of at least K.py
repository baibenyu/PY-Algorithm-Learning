# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/19 11:17'

import time
class Solution(object):
    # 方法一:滑动窗口+前缀和
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        # Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() # opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            # 题目要求最短子数组,那么前缀和的值应该尽可能接近k,即若py小于此时的栈顶,那么栈顶就不可能是最短,所以可以直接排除
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1

if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
