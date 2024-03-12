# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 10:11'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    cur = 0
    for i in range(n, n + 4):
        for j in range(n, n + 4):
            for k in range(n, n + 4):
                if i != j and j != k and i != k:
                    print(f"{i}{j}{k}", end = "")
                    cur += 1
                    if cur % 6:
                        print(end = " ")
                    else:
                        print()

    end = time.perf_counter()
    print(end - start)
