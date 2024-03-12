# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/20 14:40'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    a = [float(i) for i in input().split()]
    x1 = a[0] * math.cos(a[1])
    x2 = a[0] * math.sin(a[1])
    y1 = a[2] * math.cos(a[3])
    y2 = a[2] * math.sin(a[3])
    z1 = x1 * y1 - x2 * y2
    z2 = x1 * y2 + x2 * y1
    if -0.005 <= z1 < 0:
        z1 = '0.00'
    else:
        z1 = '%.2f' % z1
    if -0.005 <= z2 < 0:
        z2 = '+0.00i'
    elif z2 >= 0:
        z2 = '+%.2fi' % z2
    else:
        z2 = '%.2fi' % z2
    print(z1 + z2)

    end = time.perf_counter()
    print(end - start)
