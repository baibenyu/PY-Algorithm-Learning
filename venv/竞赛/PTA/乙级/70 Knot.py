# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/23 9:12'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = input()
    a = [int(i) for i in input().split()]
    a.sort()
    b = a[0] / 2 + a[1] / 2
    for i in range(2, len(a)):
        b = b / 2 + a[i] / 2
    print(int(b // 1))

    end = time.perf_counter()
    print(end - start)
