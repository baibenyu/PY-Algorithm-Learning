# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 20:29'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    cur = 0
    prefix = [2, 0, 1, 9]
    for i in range(n):
        if i < 4:
            cur = cur * 10 + prefix[i]
        else:
            temp = cur
            j = 0
            x = 4
            while x > 0:
                j += temp % 10
                temp //= 10
                x -= 1
            cur = cur * 10 + j % 10
    print(cur)

    end = time.perf_counter()
    print(end - start)
