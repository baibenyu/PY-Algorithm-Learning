# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/20 9:42'

import time

from typing import List


class Solution:
    # 方法一:环数组--滑动窗口
    # 因为只让取k个数,当数组长度大于2k时,中间部分数是一定取不到的,
    # 根据排列组合方法,可知左边可取0-k个,右边可取k-左个
    # 通过观察得知,左边取数,右边取数,实际上可以看成在一个头尾相连的环数组中取连续数组的最大值,
    # 此时题目就回归到一般的滑动窗口中了.
    # 构造一个组合的环数组,数组包含了窗口可能取到的所有组合方案.
    # 其中窗口可能取到左0右k,左1右k-1,左2右k-2...
    # 如此循环遍历所有可能取法,保留最大值
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        temp = cardPoints[len(cardPoints) - k:] + cardPoints[:k]
        cur = sum(temp[:k])
        ans = cur
        for i in range(k, len(temp)):
            cur = cur - temp[i - k] + temp[i]
            ans = max(cur, ans)
        return ans

    # 方法二:逆向滑动窗口--取左右的最大值,实际上等于取中间不取部分的最小值,又因为这部分一定连续,所以可用滑窗
    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # 滑动窗口大小为 n-k
        windowSize = n - k
        # 选前 n-k 个作为初始值
        s = sum(cardPoints[:windowSize])
        minSum = s
        for i in range(windowSize, n):
            # 滑动窗口每向右移动一格，增加从右侧进入窗口的元素值，并减少从左侧离开窗口的元素值
            s += cardPoints[i] - cardPoints[i - windowSize]
            minSum = min(minSum, s)
        return sum(cardPoints) - minSum


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
