# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/8 14:07'

import time
from typing import List


class Solution:
    # 方法一:DP
    # 完全背包,优化
    # dp表示当前容量下有几种硬币组合,每一个都等于加上,减去特定数值硬币的值
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
