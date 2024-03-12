# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 8:53'

import time


class Solution:
    # 方法一:除10取余数
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sum_up = 0
        while n:
            mul *= n % 10
            sum_up += n % 10
            n //= 10
        return mul - sum_up


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
