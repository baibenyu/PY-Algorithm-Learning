# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 19:48'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    def compare(a, b):
        if a > b:
            print(' Gai', end = '')
        elif a == b:
            print(' Ping', end = '')
        else:
            print(' Cong', end = '')


    M, X, Y = map(int, input().split())
    for i in range(99, 9, -1):
        yi = i // 10 + i % 10 * 10
        bing = abs(i - yi) / X
        if yi == Y * bing:
            print(i, end = '')
            compare(M, i)
            compare(M, yi)
            compare(M, bing)
            break
    else:
        print('No Solution')

    end = time.perf_counter()
    print(end - start)
