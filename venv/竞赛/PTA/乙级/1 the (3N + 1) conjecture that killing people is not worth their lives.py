# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 9:21'

import time


if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = 0
    while n != 1:
        ans += 1
        if n % 2:
            n = (3 * n + 1) // 2
        else:
            n /= 2
    print(ans)

    end = time.perf_counter()
    print(end - start)
