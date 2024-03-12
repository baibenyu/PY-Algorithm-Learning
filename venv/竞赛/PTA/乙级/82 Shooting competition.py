# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/25 9:55'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    n = int(input())
    winner, loser = "", ""
    maxnum, minnum = float("-inf"), float("inf")
    for i in range(n):
        ID, x, y = input().split()
        x, y = int(x), int(y)
        dis = math.sqrt(x ** 2 + y ** 2)
        if dis < minnum:
            winner = ID
            minnum = dis
        if dis > maxnum:
            loser = ID
            maxnum = dis
    print(winner, loser)

    end = time.perf_counter()
    print(end - start)
