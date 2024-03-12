# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/12 15:33'

import time


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
