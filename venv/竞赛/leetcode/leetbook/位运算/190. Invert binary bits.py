# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/4 11:14'

import time


class Solution:
    # 方法一:逐位赋值
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans <<= 1
            ans += (n & 1)
            n >>= 1
        return ans

    # 方法二:api
    def reverseBits2(self, n: int) -> int:
        string = f"{n:032b}"
        return int("".join(reversed(list(string))), 2)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
