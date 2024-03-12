# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 9:30'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, b = map(int, input().split())
    print(int(str(a * b)[::-1]))

    end = time.perf_counter()
    print(end - start)
