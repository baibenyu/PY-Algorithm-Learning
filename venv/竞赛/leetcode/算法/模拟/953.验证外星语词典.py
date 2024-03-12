# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/29 21:11'

import time
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {j: i for i, j in enumerate(order)}

        for i in range(len(words) - 1):
            if self.compare(words[i], words[i + 1], order_map):
                return False
        return True

    def compare(self, x, y, order_map):
        for i in range(len(x)):
            if i >= len(y):  # 若长度大于说明前面都相等,长度长的应该在后面,所以不符合
                return True
            if order_map[x[i]] > order_map[y[i]]:  # 小的应该在前面,所以不符合
                return True
            if order_map[x[i]] < order_map[y[i]]:
                return False
        return False  # 两字符串相等符合


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
