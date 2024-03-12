# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 20:14'

import time
from typing import List


class Solution:
    # 方法一:DP--模拟递归取石子的最优情况
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, num in enumerate(piles):  # 初始化:仅有一个数字差距固定
            dp[i][i] = num
        # 甲面对区间[i...j]时，
        #   如果甲拿nums[i]，那么变成乙面对区间[i+1...j]，这段区间内乙对甲的净胜分为dp[i+1][j]；那么甲对乙的净胜分就应该是nums[i] - dp[i+1][j]。
        #   如果甲拿nums[j]，同理可得甲对乙的净胜分为是nums[j] - dp[i][j-1]。
        for i in range(length - 2, -1, -1):  # 转移方程中用到i+1,所以要逆序遍历
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] >= 0

    # 方法二:将石子分成两堆,因为总数是偶数,即开头和结尾的石子必然属于不同组,先手可以控制对手选择的组别,只需要一直选择石子总数多的那一组即可确保获胜
    def stoneGame2(self, piles: List[int]) -> bool:
        return True


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
