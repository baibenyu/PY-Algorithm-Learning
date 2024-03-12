# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/9 20:31'

import time


class StockSpanner(object):
    # 方法一:单调栈
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
