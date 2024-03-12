# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 19:59'

import time


class Solution:
    # 方法一:奇偶规律
    # 当前值为偶数时,先手的人赢,当前值为奇数时,后手的人赢,偶数的因数可能有偶数和奇数,即偶数->奇数 or 偶数
    # 但奇数的因数只有奇数,即奇数->偶数,所以想要赢,就在偶数时将值变为奇数,奇数没得选
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

    # 方法二:DP
    # 初始值确定,按照方法一的方法来确定其它值是谁赢
    def divisorGame2(self, N: int) -> bool:
        target = [0 for i in range(N + 1)]
        target[1] = 0  # 若爱丽丝抽到1，则爱丽丝输
        if N <= 1:
            return False
        else:

            target[2] = 1  # 若爱丽丝抽到2，则爱丽丝赢
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数且target[i-j]为假（0）的话，则代表当前为真（1）
                    if i % j == 0 and target[i - j] == 0:
                        target[i] = 1
                        break
            return target[N] == 1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
