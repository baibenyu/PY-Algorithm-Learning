# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/11/5 14:11'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a, b = map(int, input().split())
    print(f"{a + b:,}")

    end = time.perf_counter()
    print(end - start)
