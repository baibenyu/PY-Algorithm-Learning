# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 20:56'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, m = map(int, input().split())
    winners = []
    for i in range(n):
        temp = map(int, input().split())
        winners.append(str(max(temp)))
    print(" ".join(winners))
    print(max(winners))

    end = time.perf_counter()
    print(end - start)
