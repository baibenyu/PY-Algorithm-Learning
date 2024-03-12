# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 17:03'

import time


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # 方法一:二分
    def guessNumber(self, n: int) -> int:
        def guess(num):  # 获取猜测结果
            return 1

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid  # 答案在区间 [left, mid] 中
            else:
                left = mid + 1  # 答案在区间 [mid+1, right] 中

        # 此时有 left == right，区间缩为一个点，即为答案
        return left


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
