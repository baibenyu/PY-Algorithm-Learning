# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 8:27'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, b = map(eval, input().split())

    q, r = a // b, a % b

    print(q, r)

    end = time.perf_counter()
    print(end - start)
