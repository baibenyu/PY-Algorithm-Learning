# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 8:57'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    d, n = input().split()
    n = int(n)
    for i in range(n - 1):
        j = 0
        k = 1
        temp = []
        while j < len(d):
            while j + k < len(d) and d[j] == d[j + k]:
                k += 1
            temp.append(d[j] + str(k))
            j += k
            k = 1
        d = "".join(temp)
    print(d)

    end = time.perf_counter()
    print(end - start)
