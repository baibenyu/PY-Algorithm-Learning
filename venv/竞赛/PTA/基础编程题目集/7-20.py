# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 16:31'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j}*{i}={i * j:<4}", end = "")
        print()

    end = time.perf_counter()
    print(end - start)
