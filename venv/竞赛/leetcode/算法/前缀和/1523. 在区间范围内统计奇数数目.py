# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/21 17:58'

import time

start = time.clock()


class Solution:
    # 方法一:前缀和,定义pre[x]为0-x内的奇数个数,那么pre(0-high)-pre(0-low-1),pre[x] = (x+1)//2
    def countOdds(self, low: int, high: int) -> int:
        pre = lambda x: (x + 1) >> 1
        return pre(high) - pre(low - 1)

    # 方法二:考虑情况--1.奇-奇 2.偶-偶 3.奇-偶
    def countOdds2(self, low: int, high: int) -> int:
        if low & 1 and high & 1:
            return 2 + (high - low - 1) // 2
        if low & 1 or high & 1:
            return 1 + (high - low - 1) // 2
        else:
            return (high - low) // 2


end = time.clock()
print(end - start)
