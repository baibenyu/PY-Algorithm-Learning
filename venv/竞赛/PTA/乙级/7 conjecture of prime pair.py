# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 20:04'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    n = int(input())

    target = [1 for i in range(n + 1)]
    target[0], target[1] = 0, 0
    # 埃式筛
    for i in range(2, int(math.sqrt(n)) + 1):
        if target[i]:
            target[i ** 2:n + 1:i] = [0] * ((n - i ** 2) // i + 1)

    temp = []
    for j in range(2, n + 1):
        if target[j]:
            temp.append(j)

    ans = 0
    for z in range(1, len(temp)):
        if temp[z] - temp[z - 1] == 2:
            ans += 1

    print(ans)

    end = time.perf_counter()
    print(end - start)
