# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/6 8:45'

import time

if __name__ == '__main__':

    a, b = map(int, input().split())
    start = time.perf_counter()
    if b == 0:
        print(0)
    else:
        lt = []
        c = 0  # 进位
        for i in range(b):
            lt.append((a * (b - i) + c) % 10)
            c = (a * (b - i) + c) // 10
            if c and i == b - 1:
                lt.append(c)
        print(''.join(list(map(str, lt[::-1]))))

    end = time.perf_counter()
    print(end - start)
