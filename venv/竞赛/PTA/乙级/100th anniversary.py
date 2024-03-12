# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 19:54'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    alumnus = set()
    for i in range(n):
        alumnus.add(input())

    m = int(input())
    count, old, strange = 0, "", ""
    for j in range(m):
        temp = input()
        if temp in alumnus:
            if not old or temp[6:14] < old[6:14]:
                old = temp
            count += 1
        if not strange or temp[6:14] < strange[6:14]:
            strange = temp

    print(count)
    if count == 0:
        print(strange)
    else:
        print(old)

    end = time.perf_counter()
    print(end - start)
