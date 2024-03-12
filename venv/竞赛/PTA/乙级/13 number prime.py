# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 10:13'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    m, n = map(int, input().split())
    isprime = [1 for i in range(105000)]
    isprime[0], isprime[1] = 0, 0
    cur = 0
    count = 0
    for j in range(2, 105000):  # 此处不能优化为根号,因为这样无法在循环中得到素数,需要另加循环
        if count < n - m + 1:
            if isprime[j]:
                isprime[j ** 2:105000:j] = [0] * ((105000 - j ** 2 - 1) // j + 1)
                cur += 1
                if cur >= m:
                    count += 1
                    if count % 10 == 0 or count == n - m + 1:
                        print(j)
                    else:
                        print(j, end = " ")
        else:
            break

    end = time.perf_counter()
    print(end - start)
