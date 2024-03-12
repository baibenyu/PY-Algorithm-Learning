# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 19:14'

import time


class Solution:
    # 方法一:数组总和 = 最大子数组和+最小子数组和,同步记录最大和最小,最后看是总和-最小大,还是最大大
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
