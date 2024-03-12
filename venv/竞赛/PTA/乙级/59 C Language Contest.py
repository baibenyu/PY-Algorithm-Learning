# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 8:59'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    isprime = [1 for _ in range(10001)]
    isprime[0] = 0
    isprime[1] = 0

    for i in range(int(math.sqrt(10000)) + 1):
        if isprime[i]:
            isprime[i ** 2:10001:i] = [0] * ((10001 - 1 - i ** 2) // i + 1)

    rank = []
    n = int(input())
    isvisited = [0 for _ in range(n)]
    for x in range(n):
        rank.append(input())

    k = int(input())
    for y in range(k):
        temp = input()
        if temp not in rank:
            print(f"{temp}: Are you kidding?")
        else:
            index = rank.index(temp)
            if isvisited[index]:
                print(f"{temp}: Checked")
            else:
                if isprime[index + 1]:
                    print(f"{temp}: Minion")
                elif index == 0:
                    print(f"{temp}: Mystery Award")
                else:
                    print(f"{temp}: Chocolate")
                isvisited[index] = 1

    end = time.perf_counter()
    print(end - start)
