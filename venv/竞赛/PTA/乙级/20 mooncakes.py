# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 9:59'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, d = map(int, input().split())
    stock = list(map(float, input().split()))
    prices = list(map(float, input().split()))

    singleprice = list(map(lambda x: x[1] / x[0], zip(stock, prices)))
    list1 = list(zip(singleprice, stock))
    list1.sort(reverse = True)
    i = 0
    ans = 0

    while d > 0 and i < n:
        ans += list1[i][0] * min(d, list1[i][1])
        d -= min(d, list1[i][1])
        i += 1

    print(f"{ans:.2f}")

    end = time.perf_counter()
    print(end - start)
