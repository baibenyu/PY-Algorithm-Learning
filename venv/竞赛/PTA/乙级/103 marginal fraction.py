# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 20:43'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    m, n = map(int, input().split())
    temp = dict()
    for i in range(m, n + 1):
        cur = math.sqrt(i * i * i - (i - 1) * (i - 1) * (i - 1))
        if cur == int(cur) and i != cur:
            temp[cur] = i
    if not temp:
        print("No Solution")
    else:
        b = 0
        now = 0
        while now < max(temp.keys()):
            b += 1
            now = b ** 2 + (b - 1) ** 2
            if now in temp.keys():
                print(temp[now], b)

    end = time.perf_counter()
    print(end - start)
