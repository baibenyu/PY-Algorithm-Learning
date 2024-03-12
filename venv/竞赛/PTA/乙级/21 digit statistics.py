# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 10:45'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = input()

    set1 = list(set(n))
    set1.sort()

    for i in range(len(set1)):
        print(f"{set1[i]}:{n.count(set1[i])}")

    end = time.perf_counter()
    print(end - start)
