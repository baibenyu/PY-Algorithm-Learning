# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/22 10:10'
import operator
import time


class Solution(object):  # Time Limit Exceeded
    # 方法一:DP+排序
    # 先针对左半边排序,dp[i]表示第i个数对的最长数对链长度
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

    # 方法二:贪心
    # 先对右半边数排序,要尽可能多的数对,那么连接要尽可能紧密,选取尽可能小的右边数进行连接
    def findLongestChain2(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
