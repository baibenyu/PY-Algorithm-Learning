# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 18:42'
import math
import time


class Solution:
    # 方法一:枚举+二分
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    # 方法二:袖珍计算器算法
    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
