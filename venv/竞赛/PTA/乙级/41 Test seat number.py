# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 9:03'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    dict1 = dict()

    for i in range(n):
        ID, tryseat, seat = input().split()
        dict1[tryseat] = (ID, seat)

    m = int(input())
    tryseats = input().split()

    for each in tryseats:
        print(dict1[each][0], dict1[each][1])

    end = time.perf_counter()
    print(end - start)
