# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/2 11:07'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = ""
    if n == 0:
        print(0)
    else:
        while n > 0:
            ans = str(n % 16) + ans
            n //= 16
        print(ans)

    end = time.perf_counter()
    print(end - start)
