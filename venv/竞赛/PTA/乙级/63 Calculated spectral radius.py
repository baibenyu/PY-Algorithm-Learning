# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 14:23'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    n = int(input())
    area = 0
    for i in range(n):
        real, virtual = map(int, input().split())
        temp = math.sqrt(real ** 2 + virtual ** 2)
        if temp > area:
            area = temp
    print(f"{area:.2f}")

    end = time.perf_counter()
    print(end - start)
