# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/18 15:21'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    from decimal import *

    n, symbol = input().split()
    n = int(n)
    line = Decimal(str(n / 2)).quantize(Decimal('0'), rounding = ROUND_HALF_UP)

    for i in range(int(line)):
        if i == 0 or i == line - 1:
            print(n * symbol)
        else:
            print(symbol + " " * (n - 2) + symbol)

    end = time.perf_counter()
    print(end - start)
