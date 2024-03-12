# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/16 9:29'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, Symbol = input().split()
    n = int(n)
    i = 1
    cur = 2 * i - 1
    while 2 * cur - 1 <= n:  # 确定最多的一行的符号个数
        i += 2
        cur += i
    cur -= i
    i -= 2
    for x in range(i, 0, -2):
        print(" " * ((i - x) // 2) + f"{Symbol * x:^}")
    for y in range(3, i + 1, 2):
        print(" " * ((i - y) // 2) + f"{Symbol * y:^}")

    print(n - 2 * cur + 1)

    end = time.perf_counter()
    print(end - start)
