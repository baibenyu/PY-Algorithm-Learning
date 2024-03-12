# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/19 8:34'

import time


class Solution:
    # 方法一:十进制转其它进制--除x倒取余法
    def convertToBase7(self, num: int) -> str:
        ans = []
        if not num:
            return "0"
        elif num > 0:
            while num > 0:
                ans.append(str(num % 7))
                num //= 7
            return "".join(ans[::-1])
        else:
            num = -num
            while num > 0:
                ans.append(str(num % 7))
                num //= 7
            return "-" + "".join(ans[::-1])


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
