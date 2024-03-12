# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/31 19:45'
import collections
import time


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = collections.deque()  # 存储能影响当前位置i的需要翻转的下标,同时代表了当前下标i已经被反转的次数
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:  # 超出首个应该反转的窗口影响范围时
                que.popleft()
            if len(que) % 2 == A[i]:  # 当 A[i] 为 0，如果 i 位置被翻转了偶数次，那么翻转后仍是 0，当前元素需要翻转；
                # 当 A[i]为 1，如果 i 位置被翻转了奇数次，那么翻转后变成 0，当前元素需要翻转。
                if i + K > N:  # 剩余元素不够反转时
                    return -1
                que.append(i)
                res += 1
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
