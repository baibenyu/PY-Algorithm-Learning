# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/2 10:50'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = 0
    while n > 0:
        ans = ans * 10 + n % 10
        n //= 10
    print(f'{ans}')

    end = time.perf_counter()
    print(end - start)
