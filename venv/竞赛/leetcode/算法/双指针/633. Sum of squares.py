# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/23 11:06'

import time

import math


class Solution:
    # 方法一:双指针+枚举
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(c ** 0.5)
        while low <= high:
            sumOf = low * low + high * high
            if sumOf == c:
                return True
            elif sumOf < c:
                low += 1
            else:
                high -= 1
        return False

    #方法二:数学
    # 费马平方和: 奇质数能表示为两个平方数之和的充分必要条件是该质数被4除余1。
    # 翻译过来就是: 当且仅当一个自然数的质因数分解中，满足4k + 3形式的质数次方数均为偶数时,该自然数才能被表示为两个平方数之和。
    # 因此我们对c进行质因数分解，再判断满足4k + 3形式的质因子的次方数是否均为偶数即可。
    def judgeSquareSum2(self, c: int) -> bool:
        for i in range(2,int(math.sqrt(c))+1):
            cnt = 0
            while c % i == 0:
                cnt += 1
                c /= i
            if i % 4 == 3 and cnt % 2 != 0:
                return False
        return c % 4 != 3


    if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
