# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 13:39'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, m = map(int, input().split())
    scores = list(map(int, input().split()))
    answer = list(map(int, input().split()))
    for i in range(n):
        cur = list(map(int, input().split()))
        temp = 0
        for j in range(m):
            if cur[j] == answer[j]:
                temp += scores[j]
        print(temp)

    end = time.perf_counter()
    print(end - start)
