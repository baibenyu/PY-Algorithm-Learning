# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 14:11'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    def gcd(m, n):  # 欧几里得算法
        m = abs(m)
        n = abs(n)
        if m < n:
            m, n = n, m
        while m % n != 0:
            r = m % n
            m = n
            n = r
        return n

    a = input().split()
    x = min(eval(a[0]), eval(a[1]))
    y = max(eval(a[0]), eval(a[1]))
    k = 1
    result = []
    while k / int(a[2]) < y:
        if k / int(a[2]) > x and gcd(k, int(a[2])) == 1:
            result.append(str(k) + '/' + str(int(a[2])))
        k += 1
    print(" ".join(result))

    end = time.perf_counter()
    print(end - start)
