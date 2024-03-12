# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/19 15:37'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            carry, num[i] = (num[i] + k % 10 + carry) // 10, (num[i] + k % 10 + carry) % 10
            k = k // 10
        while k != 0 or carry != 0:  # 加数的位数较大
            num.insert(0, (k % 10 + carry) % 10)
            k = (k + carry) // 10
            carry = (k % 10 + carry) // 10
        return num


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
