# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/19 16:31'

import time


class Solution:
    # 方法一:模拟
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
