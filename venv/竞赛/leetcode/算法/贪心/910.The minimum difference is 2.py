# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/1 15:51'

import time


class Solution(object):
    # 方法一:排序+贪心
    # 将数组升序排序,选择一个点,将该点及之前的值都加k,之后的值都减k,最大值在该点+k和最后点-k之间产生,最小值在开头+k和i+1点-k之间产生
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
