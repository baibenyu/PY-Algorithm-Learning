# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 15:09'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    m, n, a, b, t = map(int, input().split())
    for i in range(m):
        temp = list(map(int, input().split()))
        for j in range(n):
            if a <= temp[j] <= b:
                temp[j] = t
        for each in temp[:-1]:
            print(f"{each:03}", end = " ")
        print(f"{temp[-1]:03}")

    end = time.perf_counter()
    print(end - start)
