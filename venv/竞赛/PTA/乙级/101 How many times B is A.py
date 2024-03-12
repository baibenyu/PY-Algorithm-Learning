# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 19:59'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    num, d = input().split()
    d = int(d)
    cur = num[len(num) - d:] + num[:len(num) - d]
    print(f"{int(cur) / int(num):.2f}")

    end = time.perf_counter()
    print(end - start)
