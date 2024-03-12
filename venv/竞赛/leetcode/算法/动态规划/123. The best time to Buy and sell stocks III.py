# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/26 16:47'

import time
from typing import List


class Solution:
    # 方法一:DP
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]  # 定义了四种状态,第一次买入,第一次卖出,第二次买入(此处初始化可直接视为买入卖出后再买入),第二次卖出
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
