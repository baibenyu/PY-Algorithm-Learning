# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 20:42'

import time
from typing import List


class Solution:
    # 方法一:利用变量存储最大值
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxnum = sum(accounts[0])
        for each in accounts:
            maxnum = max(maxnum, sum(each))
        return maxnum


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
