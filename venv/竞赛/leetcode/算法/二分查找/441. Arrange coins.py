# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/18 19:18'

import time
class Solution:
    # 方法一:二分
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

    # 方法二:数学
    def arrangeCoins2(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)

if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
