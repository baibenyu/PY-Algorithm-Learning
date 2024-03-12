# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 14:37'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    a = input().split()
    sum1 = []
    for i in a:
        b = 0
        for j in i:
            b += int(j)
        if b not in sum1:
            sum1.append(b)
    sum1.sort()
    print(len(sum1))
    sum1 = map(str, sum1)
    print(" ".join(sum1))

    end = time.perf_counter()
    print(end - start)
