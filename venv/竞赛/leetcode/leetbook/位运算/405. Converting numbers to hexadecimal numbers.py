# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/19 9:11'

import time


class Solution:
    # 方法一:十进制转其它进制--除x倒取余法,补码+原码=2**k
    def toHex(self, num: int) -> str:
        trans = [str(i) for i in range(10)]
        trans.extend(list("abcdef"))
        ans = []
        if num == 0:
            return "0"
        elif num > 0:
            while num > 0:
                ans.append(trans[num % 16])
                num //= 16
            return "".join(ans[::-1])
        else:
            num = 2 ** 32 + num
            while num > 0:
                ans.append(trans[num % 16])
                num //= 16
            return "".join(ans[::-1])


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
