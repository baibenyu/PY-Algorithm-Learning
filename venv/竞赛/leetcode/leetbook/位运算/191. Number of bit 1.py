# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 8:44'

import time


class Solution:
    # 方法一:本身&本身-1等于去掉最右边的1
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

    # 方法二:按位进行&运算
    def hammingWeight2(self, n: int) -> int:
        sum_up = sum([1 for i in range(32) if n & (1 << i)])
        return sum_up
    # 方法三:直接bin(n).count("1")


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
