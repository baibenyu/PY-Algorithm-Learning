# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/17 16:07'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = [0 for i in range(100001)]
    maxnum = 1

    for i in range(n):
        number, score = map(int, input().split())
        ans[number] += score
        if ans[number] > ans[maxnum]:
            maxnum = number

    print(maxnum, ans[maxnum])

    end = time.perf_counter()
    print(end - start)
