# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 16:20'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    flag = False
    for y in range(100):
        for f in range(100):
            if f * 100 + y - n == 2 * y * 100 + 2 * f:
                print(f"{y}.{f}")
                flag = True
    if not flag:
        print(f"No Solution")

    end = time.perf_counter()
    print(end - start)
