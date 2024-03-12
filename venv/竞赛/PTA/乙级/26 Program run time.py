# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/16 9:10'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    from decimal import *

    clk_tck = 100
    c1, c2 = map(int, input().split())
    clock = (c2 - c1) / 100
    hour = clock // 3600
    clock -= hour * 3600
    minute = clock // 60
    second = Decimal(str(clock - 60 * minute)).quantize(Decimal('0'), rounding = ROUND_HALF_UP)

    print(f"{hour:02.0f}:{minute:02.0f}:{second:02.0f}")

    end = time.perf_counter()
    print(end - start)
