# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 11:25'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    a, b = 0, 0
    for i in range(n):
        a1, a2, b1, b2 = map(int, input().split())
        if a2 == a1 + b1 and b2 != a1 + b1:
            b += 1
        elif b2 == a1 + b1 and a2 != a1 + b1:
            a += 1

    print(a, b)

    end = time.perf_counter()
    print(end - start)
