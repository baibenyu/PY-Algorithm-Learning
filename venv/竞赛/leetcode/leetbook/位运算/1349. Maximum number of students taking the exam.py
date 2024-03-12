# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/5 12:14'

import time
from typing import List


class Solution:
    # 方法一:DP--用二进制数表示座位状态,遍历所有状态,找出可行解
    def maxStudents(self, seats: List[List[str]]) -> int:
        Row, Col = len(seats), len(seats[0])
        dp = [[-1 for _ in range(1 << Col)] for _ in range(Row + 1)]

        def check_seat(r: int, seat: int) -> bool:  # r行，这种坐法是否合理
            if seat & (seat << 1) or seat & (seat >> 1):
                return False
            for i, c in enumerate(seats[r - 1]):
                if c == '#' and (seat >> i) & 1:
                    return False
            return True

        for r in range(1, Row + 1):
            for state in range(1 << Col):
                if check_seat(r, state):  # 当前行，自己的坐法是合理的
                    people = self.cnt1(state)
                    if r == 1:
                        dp[1][state] = people  # 第一行，只管做自己
                    else:
                        for last_state in range(1 << Col):  # 上一行的坐法
                            if dp[r - 1][last_state] != -1:  # 上一行的这个坐法，是可行的
                                if (last_state & (state << 1) or last_state & (state >> 1)) == 0:  # 上一行和本行没有冲突
                                    dp[r][state] = max(dp[r][state], dp[r - 1][last_state] + people)

        return max(dp[Row])

    # ---------- 统计x的二进制中1的个数 ----------#
    def cnt1(self, x: int) -> int:
        res = 0
        while x:
            res += 1
            x &= (x - 1)
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
