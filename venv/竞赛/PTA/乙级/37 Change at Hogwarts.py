# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/18 15:35'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    isnegative = False

    p, a = input().split()
    p = list(map(int, p.split(".")))
    a = list(map(int, a.split(".")))

    ans = ((a[0] * 17 + a[1]) * 29 + a[2]) - ((p[0] * 17 + p[1]) * 29 + p[2])
    if ans < 0:
        isnegative = True
        ans = -ans

    g = ans // 17 // 29
    ans -= g * 17 * 29
    s = ans // 29
    k = ans % 29
    if isnegative:
        print(f"-{g}.{s}.{k}")
    else:
        print(f"{g}.{s}.{k}")

    end = time.perf_counter()
    print(end - start)
