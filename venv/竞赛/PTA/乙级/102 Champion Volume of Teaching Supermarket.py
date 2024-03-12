# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 20:11'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    SalesChampion, SalesChampions = ["", 0], ["", 0]
    for i in range(n):
        ID, price, sales = input().split()
        price, sales = int(price), int(sales)
        if sales >= SalesChampion[1]:
            SalesChampion[0], SalesChampion[1] = ID, sales
        if sales * price >= SalesChampions[1]:
            SalesChampions[0], SalesChampions[1] = ID, sales * price
    print(SalesChampion[0], SalesChampion[1])
    print(SalesChampions[0], SalesChampions[1])

    end = time.perf_counter()
    print(end - start)
