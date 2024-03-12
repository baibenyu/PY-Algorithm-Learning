# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/4 11:22'

import time


class Solution:
    # 方法一:均右移直至前缀相等,再左移回原位数
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

    # 方法二:找公共前缀
    # 因为n比m大,所以右边的1都会因为进位的过程中某个数会变为0,所以大于m的右边的1是无意义的,只有小于m,说明没有经过进位
    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
