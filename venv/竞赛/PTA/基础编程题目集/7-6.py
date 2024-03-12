# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/2 11:17'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    f1, i, s, f2 = input().split()
    print(f'{s} {i} {float(f1):.2f} {float(f2):.2f}')

    end = time.perf_counter()
    print(end - start)
