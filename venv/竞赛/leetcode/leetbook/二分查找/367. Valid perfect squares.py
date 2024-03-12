# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 17:10'

import time


class Solution:
    # 方法一:枚举
    def isPerfectSquare(self, num: int) -> bool:
        x = 1
        square = 1
        while square <= num:
            if square == num:
                return True
            x += 1
            square = x * x
        return False

    # 方法二:二分
    def isPerfectSquare2(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
